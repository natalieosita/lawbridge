from app.models.lawyer import ReferralRequest, ReferralResult, LawyerProfile
from app.utils.card_formatter import format_referral_card
import json

# Load mock lawyer data
with open("app/data/lawyers.json", "r", encoding="utf-8") as f:
    LAWYERS = [LawyerProfile(**lawyer) for lawyer in json.load(f)]

def refer_lawyer(request: ReferralRequest) -> ReferralResult:
    """
    Match user to a lawyer based on location and issue type.
    """
    matches = [
        lawyer for lawyer in LAWYERS
        if request.issue_type.lower() in [i.lower() for i in lawyer.specialties]
        and lawyer.location.lower() == request.location.lower()
    ]

    top_match = matches[0] if matches else None

    card = format_referral_card(request, top_match)

    return ReferralResult(
        matched_lawyer=top_match,
        referral_card=card,
        success=bool(top_match)
    )