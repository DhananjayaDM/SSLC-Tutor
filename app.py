from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.chat_service import process_question, save_memory, load_memory

app = FastAPI(
    title="Computer Science Exam Assistant"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class AskRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(req: AskRequest):

    return process_question(
        req.question
    )
class SaveRequest(BaseModel):
    question: str
    answer: str
    topic: str
    chapter: str


@app.post("/save")
def save(req: SaveRequest):

    saved = save_memory(
        question=req.question,
        answer=req.answer,
        topic=req.topic,
        chapter=req.chapter
    )

    return {
        "saved": saved
    }
class ChapterRequest(BaseModel):
    chapter: str

@app.post("/chapter")
def get_chapter(req: ChapterRequest):

    file_path = os.path.join(
        "summarization",
        f"{req.chapter}.json"
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Chapter not found"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    return data

@app.get("/chapters")
def get_chapters():

    files = [
        f.replace(".json", "")
        for f in os.listdir("summarization")
        if f.endswith(".json")
    ]

    return {
        "chapters": sorted(files)
    }    

@app.get("/saved")
def get_saved():

    data = load_memory()

    return data   