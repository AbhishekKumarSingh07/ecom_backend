from fastapi import FastAPI
from ecom_backend import auth_router, user_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)# from ecom_backend.apis import auth_router, user_router



