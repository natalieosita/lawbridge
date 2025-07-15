from fastapi import APIRouter, Query
from app.services.rights_finder import find_matching_articles
from app.utils.card_formatter import format_explainer_card

router = APIRouter()

@router.get("/ask-rights")
def ask_rights(query: str = Query(..., description="Ask a legal question")):
    raw_results = find_matching_articles(query)
    formatted = [format_explainer_card(r) for r in raw_results]
    return {"query": query, "results": formatted}
