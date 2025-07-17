from typing import Dict, List
from app.services.compliance_engine import check_compliance
from app.utils.card_formatter import format_situation_card
from app.models.situation import SituationInput, AssessmentResult

def assess_situation(situation: SituationInput) -> AssessmentResult:
    """
    Assess a real-life situation for constitutional compliance.
    Returns a structured civic card with legal status, advice, and referral info.
    """
    # Step 1: Run compliance check
    compliance_result = check_compliance(situation.description)

    # Step 2: Determine legal status
    if compliance_result.is_compliant:
        status = "legal"
        advice = ["Your situation appears to comply with the Constitution."]
        refer_to_lawyer = False
    elif compliance_result.is_unclear:
        status = "unclear"
        advice = [
            "The legality of your situation is ambiguous.",
            "Consider consulting a lawyer for clarification."
        ]
        refer_to_lawyer = True
    else:
        status = "illegal"
        advice = [
            "Your situation may violate constitutional principles.",
            "Consider the following steps to make it compliant:"
        ] + compliance_result.suggested_remedies
        refer_to_lawyer = True

    # Step 3: Format civic card
    card = format_situation_card(
        description=situation.description,
        status=status,
        advice=advice,
        refer_to_lawyer=refer_to_lawyer
    )

    # Step 4: Return structured result
    return AssessmentResult(
        status=status,
        advice=advice,
        refer_to_lawyer=refer_to_lawyer,
        civic_card=card
    )