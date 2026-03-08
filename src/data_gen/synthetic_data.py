from pydantic import BaseModel, Field
from typing import List
from uuid import UUID
from datetime import datetime

class PredictionRequest(BaseModel):
    sleep_hours: float = Field(..., ge=0, le=12, description="Total sleep duration in hours.")
    study_minutes: int = Field(..., ge=0, le=1000, description="Focused study time in minutes.")
    break_minutes: int = Field(..., ge=0, le=600, description="Break duration in minutes.")
    phone_usage_hours: float = Field(..., ge=0, le=16, description="Screen time in hours.")
    mood: int = Field(..., ge=1, le=10, description="Mood rating (1–10).")
    stress_level: int = Field(..., ge=1, le=10, description="Stress level (1–10).")
    exercise_minutes: int = Field(..., ge=0, le=300, description="Exercise duration in minutes.")
    caffeine_mg: int = Field(..., ge=0, le=1000, description="Daily caffeine intake in mg.")
    tasks_completed: int = Field(..., ge=0, le=50, description="Number of tasks completed.")
    day_of_week: int = Field(..., ge=1, le=7, description="Day of week (1=Mon … 7=Sun).")

    class Config:
        json_schema_extra = {
            "example": {
                "sleep_hours": 7.0,
                "study_minutes": 120,
                "break_minutes": 45,
                "phone_usage_hours": 2.5,
                "mood": 7,
                "stress_level": 4,
                "exercise_minutes": 30,
                "caffeine_mg": 150,
                "tasks_completed": 5,
                "day_of_week": 3
            }
        }
