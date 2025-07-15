# app/routes/smart_compliance.py

from fastapi import APIRouter, Query
from sentence_transformers import SentenceTransformer, util
import json

router = APIRouter()
model = SentenceTransformer('all-MiniLM-L6-v2')

with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

def format_compliance_verdict(match: dict) -> dict:
    outcome_map = {
        "allowed": ("✅ Compliant", "shield-check", "green"),
        "restricted": ("❌ Not Compliant", "shield-exclamation", "red"),
        "uncertain": ("⚠️ Uncertain", "question-mark-circle", "yellow")
    }
    verdict_text, icon, color = outcome_map.get(match["verdict"], outcome_map["uncertain"])

    referral = {
        "name": "Adv. Wanjiku N.",
        "location": "Kiambu County",
        "email": "wanjiku@lawnet.ke",
        "specialty": "Constitutional Law",
        "nextSteps": "This issue may require human legal advice."
    } if match["score"] < 0.5 else None

    return {
        "cardType": "compliance",
        "verdict": verdict_text,
        "reasoning": match["summary"],
        "legal_refs": [f"Article {match['article_number']}"],
        "confidence": round(match["score"], 2),
        "action_suggestion": "Consult a lawyer for clarification." if match["verdict"] == "restricted" else "You're operating within legal bounds.",
        "icon": icon,
        "color": color,
        "lawyerReferral": referral
    }

@router.get("/check-compliance")
def check_smart_compliance(
    input: str = Query(..., description="Describe the legal action or scenario")
):
    input_embedding = model.encode(input, convert_to_tensor=True)
    matches = []

    for article in ARTICLES:
        title = article.get("title", "")
        text = article.get("text", "")
        full_text = f"{title} {text}"

        if not text:
            continue

        article_embedding = model.encode(full_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(input_embedding, article_embedding).item()

        if score > 0.45:
            verdict = "allowed"
            if any(kw in text.lower() for kw in ["may not", "shall not", "prohibited", "illegal"]):
                verdict = "restricted"

            matches.append({
                "article_number": article.get("article_number"),
                "title": title,
                "chapter": article.get("chapter", "N/A"),
                "score": score,
                "verdict": verdict,
                "summary": text[:300] + "..." if len(text) > 300 else text
            })

    if not matches:
        return format_compliance_verdict({
            "verdict": "uncertain",
            "score": 0.0,
            "summary": "Couldn't find a strong constitutional match. Please rephrase or consult a lawyer.",
            "article_number": "N/A"
        })

    best_match = sorted(matches, key=lambda x: x["score"], reverse=True)[0]
    return format_compliance_verdict(best_match)