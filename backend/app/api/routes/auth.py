from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.database import get_db

from app.schemas.auth import LoginSchema, Token
from app.core.jwt_handler import create_access_token
from app.api.routes.deps import get_current_user   


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserOut)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    print("PASSWORD RECEIVED >>>", payload.password, "LEN:", len(payload.password.encode()))

    # 1. Check if user already exists
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Hash the password
    hashed_pw = hash_password(payload.password)

    # 3. Create new user instance
    new_user = User(
        email=payload.email,
        hashed_password=hashed_pw
    )

    # 4. Save user in DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 5. Return safe user output
    return new_user

@router.post("/login", response_model=Token)
def login_user(payload: LoginSchema, db: Session = Depends(get_db)):
    

    user = db.query(User).filter(User.email == payload.email).first()
    print("USER FROM DB:", user)

    if not user:
        print("NO USER FOUND")
        raise HTTPException(status_code=401, detail="Invalid email or password")

    print("HASH IN DB:", user.hashed_password)
    print("VERIFY_RESULT:", verify_password(payload.password, user.hashed_password))

    if not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(
        data={"sub": str(user.id), "email": user.email}
    )

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_current_user)):
    return user
