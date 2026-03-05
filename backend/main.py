from fastapi import FastAPI
from pydantic import BaseModel
from .analyzer import analyze_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Дозволяємо фронтенду робити запити
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze(request: TextRequest):
    return analyze_text(request.text)