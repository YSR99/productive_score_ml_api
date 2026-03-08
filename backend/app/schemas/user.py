from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def password_length_check(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must be 72 characters or fewer.")
        return v


# ----------------------------
# Schema for returning user info (safe output)
# ----------------------------
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
