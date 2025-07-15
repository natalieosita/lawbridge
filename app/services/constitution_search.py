from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

# Precompute embeddings for all articles (title + text)
ARTICLE_EMBEDS = [
    model.encode(article.get("title", "") + " " + article.get("text", ""), convert_to_tensor=True)
    for article in ARTICLES
]

def search_constitution(query, top_k=3):
    """
    Search for the most relevant constitutional articles for a given query using semantic similarity.
    """
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = [util.pytorch_cos_sim(query_embedding, art_emb).item() for art_emb in ARTICLE_EMBEDS]
    results = [
        {**article, "score": score}
        for article, score in zip(ARTICLES, scores)
    ]
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    return sorted_results[:top_k]