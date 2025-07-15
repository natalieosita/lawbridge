from fastapi import APIRouter, Query
from app.services.explainer_distilbart import explain_article_distilbart
from app.utils.card_formatter import format_explainer_card

router = APIRouter()

@router.get("/explain-article-ai")
def get_ai_explainer(
    article: int = Query(..., description="Article number to explain"),
    tone: str = Query("neutral", description="Explanation tone: student, policy, civic, formal, or neutral")
):
    """
    Get an AI-generated explanation of a constitutional article in a specified tone.
    """
    resp = explain_article_distilbart(article, tone)
    if resp.get("error"):
        return resp
    return format_explainer_card(resp)