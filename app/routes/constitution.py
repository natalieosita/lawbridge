from fastapi import APIRouter, Query
from app.services.constitution_search import search_constitution

router = APIRouter()

@router.get("/search-article")
def search_article(q: str = Query(...)):
    """
    Search for relevant constitutional articles based on a query string.
    """
    matches = search_constitution(q)
    if not matches:
        return {"query": q, "results": []}
    return {
        "query": q,
        "results": [
            {
                "article_number": a.get("article_number"),
                "title": a.get("title"),
                "summary": a.get("text", "")[:400] + ("..." if len(a.get("text", "")) > 400 else ""),
                "score": round(a.get("score", 0), 4),
                "chapter": a.get("chapter", "N/A")
            }
            for a in matches
        ]
    }