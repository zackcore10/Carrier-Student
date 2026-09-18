from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

from ai.reccomendation import recommend_career


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


def save_student(data, career):

    connection = sqlite3.connect("careerai.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, programming, math, communication, interest, experience, recommended_career)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.name,
        data.programming,
        data.math,
        data.communication,
        data.interest,
        data.experience,
        career
    ))

    connection.commit()
    connection.close()


@app.get("/")
def home():

    return {
        "message": "CareerAI Backend is running!"
    }


@app.post("/assessment")
def assessment(data: Student):

    career = recommend_career(
        data.programming,
        data.math,
        data.communication,
        data.interest,
        data.experience
    )

    save_student(data, career)

    return {
        "message": "Assessment received successfully!",
        "student": data,
        "recommended_career": career
    }