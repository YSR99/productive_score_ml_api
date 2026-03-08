from pydantic import BaseModel, Field

class ProductivityInput(BaseModel):
    sleep_hours: float
    study_minutes: float
    break_minutes: float
    phone_usage_hours: float
    mood: int = Field(ge=1, le=5)
    stress_level: float
    exercise_minutes: float
    caffeine_mg: float
    tasks_completed: int
    day_of_week: str
