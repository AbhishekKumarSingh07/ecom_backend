from fastapi import APIRouter, status, Depends, HTTPException
from ecom_backend.database import get_db_connection
from ecom_backend.schema.user_schema import SignUpUser, LoginUser, UpdateUser
from ecom_backend.models.user_model import User
from sqlalchemy.orm import Session
from ecom_backend.validators.user_validations import validate_signup
from fastapi.security import OAuth2PasswordRequestForm
from ecom_backend.utils import verify_password, get_password_hash, create_access_token, create_refresh_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
@validate_signup
async def signup(user: SignUpUser, db: Session = Depends(get_db_connection)):
    hashed_password = get_password_hash(user.password)
    new_user: User = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        user_name=user.user_name,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: LoginUser, db: Session = Depends(get_db_connection)):
    login_user = db.query(User).filter(User.user_name == user.user_name).first()
    if not login_user or not verify_password(user.password, login_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    return {
        "access_token": create_access_token(login_user.email),
        "refresh_token": create_refresh_token(login_user.email)
    }
