from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your constitution
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

def check_smart_compliance(action: str, top_n: int = 3, threshold: float = 0.45) -> dict:
    action_embedding = model.encode(action, convert_to_tensor=True)
    matches = []

    for article in ARTICLES:
        title = article.get("title", "")
        text = article.get("text", "")
        full_text = f"{title} {text}"

        if not text:
            continue

        a_embedding = model.encode(full_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(action_embedding, a_embedding).item()

        if score > threshold:
            verdict = "allowed"
            if any(kw in text.lower() for kw in ["may not", "shall not", "prohibited", "illegal", "not allowed"]):
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

    top_match = sorted(matches, key=lambda x: x["score"], reverse=True)[0]
    return format_compliance_verdict(top_match)