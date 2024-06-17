from pydantic import BaseModel, Field
from typing import Optional


class SignUpUser(BaseModel):
    first_name: str = Field(min_length=1, description="Enter your First Name")
    last_name: str = Field(min_length=1, description="Enter your Last Name")
    email: str = Field(min_length=4)
    user_name: str = Field(
        min_length=1,
        description="Accepts only lowercase letters, numbers, " "and underscores.",
    )
    password: str = Field(min_length=4)
    repeat_password: str = Field(min_length=4)
    is_admin: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "first_name": "Abhishek",
                "last_name": "Singh",
                "email": "abhishek@gmail.com",
                "user_name": "abhishek_singh",
                "password": "Abcdefgh",
                "repeat_password": "Abcdefgh",
            }
        }


class JWTSecretKey(BaseModel):
    auth_jwt_secret_key: str = ""


class LoginUser(BaseModel):
    user_name: str = Field(min_length=1)
    password: str = Field(min_length=4)


class UpdateUser(BaseModel):
    first_name: str = Field(min_length=1, description="Enter your First Name")
    last_name: str = Field(min_length=1, description="Enter your Last Name")
    password: str = Field(min_length=4)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "first_name": "Abhishek",
                "last_name": "Singh",
                "password": "Abcdefgh",
            }
        }
