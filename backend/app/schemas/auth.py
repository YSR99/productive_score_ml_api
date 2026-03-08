from pydantic import BaseModel, EmailStr


# ------------------------------------
# LOGIN INPUT SCHEMA
# ------------------------------------
class LoginSchema(BaseModel):
    email: EmailStr
    password: str


# ------------------------------------
# TOKEN OUTPUT SCHEMA
# ------------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
