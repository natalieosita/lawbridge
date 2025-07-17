from transformers import pipeline
import json
import os

print("[DEBUG] explainer_distilbart.py imported")

# Load summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Load Constitution
with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

CACHE_PATH = "app/data/explainer_cache.json"

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def explain_article_distilbart(article_number: int, tone: str = "neutral") -> dict:
    print("[DEBUG] explain_article_distilbart called with:", article_number, tone)

    cache = load_cache()
    key = f"{article_number}_{tone}"

    # ✅ Return cached formatted card if present
    if key in cache:
        print("[DEBUG] Cache hit for", key)
        return cache[key]

    # 📖 Lookup article
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

            # ✅ Build civic card directly
            formatted = {
                "cardType": "explainer",
                "articleNumber": article_number,
                "title": title,
                "tone": tone,
                "icon": "information-circle",
                "tag": "Legal Educator",
                "color": "teal",
                "summary": summary,
                "rawTextPreview": raw_text,
                "confidence": 0.65,
                "lawyerReferral": {
                    "name": "Adv. Wanjiku N.",
                    "location": "Kiambu County",
                    "email": "wanjiku@lawnet.ke",
                    "specialty": "Land & Constitutional Law",
                    "nextSteps": "This issue may require human legal advice."
                },
                "language": "en",
                "references": [
                    {
                        "type": "foundational",
                        "label": "Constitution of Kenya (2010)",
                        "link": "https://www.kenyalaw.org/kl/index.php?id=398"
                    }
                ]
            }

            # 💾 Save to cache
            cache[key] = formatted
            save_cache(cache)

            print("[DEBUG] Returning formatted new card")
            return formatted

    print("[DEBUG] Article not found:", article_number)
    return {"error": f"Article {article_number} not found."}