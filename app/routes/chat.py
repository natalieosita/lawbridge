# app/routes/chat.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chatbot_engine import handle_chat_turn

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    intent: str = "auto"

@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    response = handle_chat_turn(req.message, intent=req.intent)
    return response