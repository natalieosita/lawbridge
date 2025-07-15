import json
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.explainer_distilbart import explain_article_distilbart

# Load articles
with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

# Embed model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# One-time embedding (or cache later)
ARTICLE_EMBEDS = [embedder.encode(article["text"]) for article in ARTICLES]

def find_matching_articles(query: str, top_k: int = 3):
    query_vec = embedder.encode(query)
    scores = cosine_similarity([query_vec], ARTICLE_EMBEDS)[0]

    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    matches = [ARTICLES[i] for i in top_indices]

    results = []
    for match in matches:
        article_num = int(match.get("article_number"))
        summary = explain_article_distilbart(article_num)
        if not summary.get("error"):
            results.append(summary)

    return results