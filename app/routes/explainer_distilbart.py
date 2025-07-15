from fastapi import APIRouter, Query
from app.services.explainer_distilbart import explain_article_distilbart  # or use explain_article_pegasus if Pegasus is active

router = APIRouter()

@router.get("/explain-article-ai")
def get_ai_explainer(article: int = Query(...), tone: str = Query("neutral")):
    return explain_article_distilbart(article, tone)