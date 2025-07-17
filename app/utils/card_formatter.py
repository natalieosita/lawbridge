from app.utils.reference_db import global_references

# Constants
REFERRAL_THRESHOLD = 0.7
DEFAULT_TONE = "neutral"

TONE_ICON_MAP = {
    "student": ("book-open", "green"),
    "formal":  ("clipboard-list", "gray"),
    "civic":   ("user-group", "blue"),
    "policy":  ("document-report", "purple"),
    "neutral": ("information-circle", "teal")
}

DEFAULT_LAWYER = {
    "name": "Adv. Wanjiku N.",
    "location": "Kiambu County",
    "email": "wanjiku@lawnet.ke",
    "specialty": "Land & Constitutional Law",
    "nextSteps": "This issue may require human legal advice."
}

def format_explainer_card(resp: dict) -> dict:
    """
    Format a civic card for AI-generated article explanations.
    """
    tone = resp.get("tone", DEFAULT_TONE)
    icon, color = TONE_ICON_MAP.get(tone, TONE_ICON_MAP[DEFAULT_TONE])
    confidence_score = 0.65 if tone in ["formal", "neutral"] else 0.9

    lawyer_referral = DEFAULT_LAWYER if confidence_score < REFERRAL_THRESHOLD else None

    formatted_response = {
        "cardType": "explainer",
        "articleNumber": resp.get("article_number", "N/A"),
        "title": resp.get("title", ""),
        "tone": tone,
        "icon": icon,
        "tag": "Legal Educator",
        "color": color,
        "summary": resp.get("summary", ""),
        "rawTextPreview": resp.get("raw_text", ""),
        "confidence": confidence_score,
        "lawyerReferral": lawyer_referral,
        "language": "en",
        "references": global_references
    }

    return formatted_response
def format_situation_card(description: str, status: str, advice: list, refer_to_lawyer: bool) -> dict:
    """
    Format a civic card summarizing the legal assessment of a situation.
    """
    status_label = {
        "legal": "✅ Legal",
        "illegal": "❌ Potentially Illegal",
        "unclear": "⚠️ Legality Unclear"
    }.get(status, "⚠️ Unknown Status")

    card = {
        "cardType": "situationAssessment",
        "title": "Legal Situation Assessment",
        "description": description,
        "status": status_label,
        "advice": advice,
        "referral": "Recommended to consult a lawyer." if refer_to_lawyer else "No referral needed.",
        "nextSteps": advice if status != "legal" else ["No further action required."]
    }

    return card
def format_referral_card(request, lawyer) -> dict:
    if not lawyer:
        return {
            "cardType": "lawyerReferral",
            "title": "No Match Found",
            "message": f"No verified lawyers found for '{request.issue_type}' in {request.location}.",
            "suggestion": "Try broadening your location or issue type."
        }

    return {
        "cardType": "lawyerReferral",
        "title": "Recommended Legal Expert",
        "issueType": request.issue_type,
        "location": request.location,
        "lawyer": {
            "name": lawyer.name,
            "email": lawyer.email,
            "phone": lawyer.phone,
            "specialties": lawyer.specialties,
            "verified": lawyer.verified
        },
        "nextSteps": "You can reach out directly or request a formal consultation."
    }