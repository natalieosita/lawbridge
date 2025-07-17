from fastapi import APIRouter, Query
from app.services.explainer_distilbart import explain_article_distilbart

router = APIRouter()

@router.get("/explain-article-ai")
def get_ai_explainer(
    article: int = Query(..., description="Article number to explain"),
    tone: str    = Query("neutral", description="Tone: student, policy, civic, formal, or neutral")
):
    """
    Return a formatted civic card explanation for a constitutional article.
    """
    return explain_article_distilbart(article, tone)