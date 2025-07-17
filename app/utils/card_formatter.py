from app.utils.reference_db import global_references, reference_lookup

def format_explainer_card(resp: dict) -> dict:
    confidence_score = 0.65 if resp["tone"] in ["formal", "neutral"] else 0.9

    tone_icon_map = {
        "student": ("book-open", "green"),
        "formal":  ("clipboard-list", "gray"),
        "civic":   ("user-group", "blue"),
        "policy":  ("document-report", "purple"),
        "neutral": ("information-circle", "teal")
    }
    icon, color = tone_icon_map.get(resp["tone"], tone_icon_map["neutral"])

    lawyer_referral = {
        "name": "Adv. Wanjiku N.",
        "location": "Kiambu County",
        "email": "wanjiku@lawnet.ke",
        "specialty": "Land & Constitutional Law",
        "nextSteps": "This issue may require human legal advice."
    } if confidence_score < 0.7 else None

    summary = resp["summary"]
    article_refs = reference_lookup.get(resp["article_number"], [])
    all_refs = global_references + article_refs
    formatted_response = {
        "cardType": "explainer",
        "articleNumber": resp["article_number"],
        "title": resp["title"],
        "tone": resp["tone"],
        "icon": icon,
        "tag": "Legal Educator",
        "color": color,
        "summary": summary,
        "rawTextPreview": resp["raw_text"],
        "confidence": confidence_score,
        "lawyerReferral": lawyer_referral,
        "language": "en",
        "references": all_refs
    }
    # Optionally keep this debug print:
    # print("[DEBUG] Formatter output:", formatted_response)
    return formatted_response