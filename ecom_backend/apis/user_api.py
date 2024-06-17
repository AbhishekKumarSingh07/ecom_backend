from fastapi import APIRouter, status, Depends, HTTPException
from ecom_backend.database import get_db_connection
from ecom_backend.schema.user_schema import SignUpUser, LoginUser, UpdateUser
from ecom_backend.models.user_model import User
from sqlalchemy.orm import Session
from ecom_backend.validators.user_validations import validate_user_existence

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_user_list(db: Session = Depends(get_db_connection)):
    users = db.query(User).all()
    return users


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
@validate_user_existence
async def get_user_by_id(user_id: int, db: Session = Depends(get_db_connection)):

    # validate_user_existence(user_id)
    user = db.query(User).filter(User.id == user_id).first()

    return user


@user_router.patch("/{user_id}", status_code=status.HTTP_200_OK)
@validate_user_existence
async def update_user(
    user_id: int, user_update: UpdateUser, db: Session = Depends(get_db_connection)
):
    # validate_user_existence(user_id)
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
@validate_user_existence
async def delete_user(user_id: int, db: Session = Depends(get_db_connection)):
    # validate_user_existence(user_id)
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return get_user_list
