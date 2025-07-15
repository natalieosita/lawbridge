import json
import re

with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

def explain_article(article_number: int, tone: str = "neutral") -> dict:
    for article in ARTICLES:
        if article.get("article_number") == str(article_number):
            title = article.get("title", "")
            text = article.get("text", "")

            # Simple rule-based explainer (can upgrade later)
            explanation = f"**{title}** — This article ensures: "

            if re.search(r"citizen|non-citizen|land", text.lower()):
                explanation += "rules around citizenship and land ownership."
            elif "expression" in text.lower():
                explanation += "freedom of speech, with exceptions for hate speech."
            elif "assembly" in text.lower():
                explanation += "the right to peaceful protest and petitioning authorities."
            else:
                explanation += "a constitutional right or duty — full reading recommended."

            return {
                "article_number": article_number,
                "title": title,
                "summary": explanation,
                "tone": tone,
                "raw_text": text
            }

    return {
        "error": f"Article {article_number} not found. Try a number between 1 and {len(ARTICLES)}."
    }