import os
from dotenv import load_dotenv

load_dotenv()


JWT_SECRET_KEY = os.getenv("SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
