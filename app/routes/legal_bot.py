from fastapi import APIRouter, Query
from app.services.nlp_engine import answer_legal_question

router = APIRouter()

@router.get("/ask-legal-question")
def ask_legal(q: str = Query(...)):
    return answer_legal_question(q)