import re
from sentence_transformers import SentenceTransformer, util
import json

# Load articles and model
with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)
model = SentenceTransformer('all-MiniLM-L6-v2')
ARTICLE_EMBEDS = [
    model.encode(article.get("title", "") + " " + article.get("text", ""), convert_to_tensor=True)
    for article in ARTICLES
]

def check_compliance(user_input, top_k=1):
    """
    Checks compliance by semantic similarity to constitutional articles.
    """
    # 1. Try rule-based first for high precision
    for rule in RULES:
        if re.search(rule["pattern"], user_input, re.IGNORECASE):
            return {
                "verdict": rule["verdict"],
                "article_reference": f"Article {rule['article_number']}",
                "title": rule["title"],
                "summary": rule["summary"],
                "method": "rule-based"
            }

    # 2. Fallback to semantic search
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = [util.pytorch_cos_sim(query_embedding, art_emb).item() for art_emb in ARTICLE_EMBEDS]
    top_idx = max(range(len(scores)), key=lambda i: scores[i])
    top_article = ARTICLES[top_idx]
    summary = top_article.get("text", "")[:350] + "..." if len(top_article.get("text", "")) > 350 else top_article.get("text", "")

    return {
        "verdict": "refer",
        "article_reference": f"Article {top_article.get('article_number', 'N/A')}",
        "title": top_article.get("title", ""),
        "summary": summary,
        "method": "semantic"
    }