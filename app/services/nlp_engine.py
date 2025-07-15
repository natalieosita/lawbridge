from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

def answer_legal_question(question, threshold=0.45):
    q_embedding = model.encode(question, convert_to_tensor=True)
    results = []

    for article in ARTICLES:
        # Use .get() to avoid KeyError if fields are missing
        title = article.get("title", "")
        text = article.get("text", "")
        content = title + " " + text
        a_embedding = model.encode(content, convert_to_tensor=True)
        score = util.pytorch_cos_sim(q_embedding, a_embedding).item()
        if score > threshold:
            results.append({**article, "score": score})

    if not results:
        return {
            "answer": "I'm not confident I can find a constitutional match. Please try rephrasing or consult a lawyer.",
            "article_reference": None,
            "summary": None
        }

    top_matches = sorted(results, key=lambda x: x["score"], reverse=True)[:3]

    return {
    "answer": f"I found {len(top_matches)} relevant constitutional articles for your question.",
    "matches": [
        {
            "article_number": match.get("article_number"),
            "title": match.get("title"),
            "score": round(match["score"], 4),
            "summary": match.get("text", "")[:300] + "..." if len(match.get("text", "")) > 300 else match.get("text", ""),
            "chapter": match.get("chapter", "N/A")
        } for match in top_matches
    ]
}