from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime

from app.schemas.predict import (
    PredictionRequest,
    PredictionResponse,
    ErrorResponse
)

from app.api.routes.deps import get_current_user
from app.database import get_db
from app.services.predictor import model_service
from app.services.recommendations import generate_tips
from app.models.prediction_log import PredictionLog


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "",
    response_model=PredictionResponse,
    responses={500: {"model": ErrorResponse}}
)
def predict_productivity(
    payload: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Prediction Endpoint
    - JWT protected
    - Validates input using PredictionRequest
    - Runs ML model inference
    - Generates tips
    - Logs prediction to database
    """

    try:
        # 1. Convert Pydantic to dict
        input_data = payload.dict()

        # 2. Run model inference
        predicted_score = model_service.predict(input_data)

        # 3. Generate personalized tips
        recommended_tips = generate_tips(predicted_score)

        # 4. Create a unique request ID
        request_id = str(uuid4())

        # 5. Log prediction into DB
        log_entry = PredictionLog(
            user_id=current_user.id,
            request_id=request_id,
            input_data=input_data,
            prediction_score=predicted_score,
        )
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)

        # 6. Send response
        return PredictionResponse(
            request_id=request_id,
            productivity_score=predicted_score,
            personalized_tips=recommended_tips,
            timestamp=log_entry.created_at
        )

    except Exception as e:
        print("Prediction Error:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Model inference failed. Please try again later."
        )
