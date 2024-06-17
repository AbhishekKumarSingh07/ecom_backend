from fastapi import HTTPException, status
from functools import wraps
from ecom_backend.models.user_model import User


def validate_signup(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        db = kwargs.get('db')
        user = kwargs.get('user')
        email = user.email
        username = user.user_name

        if db.query(User).filter(User.email == email).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email Id already exist!"
            )

        if db.query(User).filter(User.user_name == username).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username already exist"
            )

        if user.password != user.repeat_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Password mismatch"
            )

        return await func(*args, **kwargs)

    return wrapper


def validate_user_existence(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user_id = kwargs.get('user_id')

        db = kwargs.get('db')
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID: {user_id} not found!",
            )

        return await func(*args, **kwargs)

    return wrapper

# async def validate_signup(user: SignUpUser, db: Session = Depends(get_db_connection)):
#     email = user.email
#     username = user.user_name
#
#     if db.query(User).filter(User.email == email).first():
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="Email Id already exist!"
#         )
#
#     if db.query(User).filter(User.user_name == username).first():
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="Username already exist"
#         )
#
#     if user.password != user.repeat_password:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Password mismatch"
#         )
#
#
# async def validate_user_existence(user_id: int, db: Session = Depends(get_db_connection)):
#     user = db.query(User).filter(User.id == user_id).first()
#
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with ID: {user_id} not found!",
#         )
