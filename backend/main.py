from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    name: str
    programming: str
    math: str
    communication: str
    interest: str
    experience: str


@app.get("/")
def home():
    return {
        "message": "CareerAI Backend is running!"
    }


@app.post("/assessment")
def assessment(data: Student):

    if data.interest == "Artificial Intelligence":
        career = "AI/ML Engineer"
    elif data.interest == "Web Development":
        career = "Full Stack Developer"
    elif data.interest == "Data Science":
        career = "Data Scientist"
    elif data.interest == "Cyber Security":
        career = "Cyber Security Analyst"
    elif data.interest == "Cloud Computing":
        career = "Cloud Engineer"
    else:
        career = "Career not found"

    return {
        "message": "Assessment received successfully!",
        "student": data,
        "recommended_career": career
    }