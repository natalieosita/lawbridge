from transformers import pipeline
import json, os

# Load summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Load Constitution
with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

CACHE_PATH = "app/data/explainer_cache.json"

def load_cache():
    """Load the explanation cache from disk."""
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save the explanation cache to disk."""
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def explain_article_distilbart(article_number: int, tone: str = "neutral") -> dict:
    """
    Generate or retrieve a summary explanation for a constitutional article in a specified tone.
    """
    cache = load_cache()
    key = f"{article_number}_{tone}"

    # 🔒 Check cache first
    if key in cache:
        return cache[key]

    # 📖 Lookup article text
    for article in ARTICLES:
        if article.get("article_number") == str(article_number):
            title = article.get("title", "")
            raw_text = article.get("text", "")

            tone_hint = {
                "student": "Explain like a high school teacher guiding students.",
                "policy": "Summarize with bullet points for lawmakers.",
                "civic": "Make this clear for citizens unfamiliar with legal terms.",
                "formal": "Use professional, legal-style summary.",
                "neutral": "Just summarize clearly with no stylistic twist."
            }.get(tone, "Summarize clearly.")

            input_text = f"{tone_hint} Title: {title}. Article Text: {raw_text}"
            summary = summarizer(input_text, max_length=80, min_length=30, do_sample=False)[0]["summary_text"]

            response = {
                "article_number": article_number,
                "title": title,
                "summary": summary,
                "tone": tone,
                "raw_text": raw_text
            }

            # 💾 Save to cache
            cache[key] = response
            save_cache(cache)

            return response

    return {"error": f"Article {article_number} not found."}