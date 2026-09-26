import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Routes.studentroutes import router

app = FastAPI()

cors_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "*").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def greet():
    return {"message": "Student Management API is running"}