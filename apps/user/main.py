import os
import time

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.config import CORS_ORIGINS, APP_TZ, APP_PORT, APP_ENV
from src import user_routers

user_app = FastAPI(title="User App", version="0.0.1")

# Configure CORS
user_app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure timezone
os.environ["tz"] = APP_TZ
time.tzset()

# Import routes
user_app.include_router(user_routers)


if __name__ == "__main__":
    uvicorn.run(
        "main:user_app",
        host="0.0.0.0",
        port=APP_PORT,
        reload=bool(APP_ENV != "production"),
        use_colors=True,
    )