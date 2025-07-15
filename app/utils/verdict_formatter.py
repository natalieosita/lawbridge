# app/utils/verdict_formatter.py
def format_compliance_verdict(result: dict) -> dict:
    outcome_icon = "shield-check" if result["verdict"] == "Compliant" else "shield-exclamation"
    color = "green" if result["verdict"] == "Compliant" else "red"

    return {
        "cardType": "compliance",
        "verdict": result["verdict"],  # "✅ Compliant" or "❌ Not Compliant"
        "reasoning": result["reasoning"],
        "legal_refs": result["legal_refs"],  # e.g. ["Article 65"]
        "confidence": result.get("confidence", 0.85),
        "action_suggestion": result.get("action_suggestion", "Consider legal consultation."),
        "icon": outcome_icon,
        "color": color
    }