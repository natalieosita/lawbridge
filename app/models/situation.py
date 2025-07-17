from pydantic import BaseModel
from typing import List, Optional

class SituationInput(BaseModel):
    """
    Input schema for assessing a real-life situation.
    """
    description: str  # A plain-language description of the user's situation


class AssessmentResult(BaseModel):
    """
    Output schema for the result of a situation assessment.
    """
    status: str  # One of: "legal", "illegal", "unclear"
    advice: List[str]  # Actionable guidance or next steps
    refer_to_lawyer: bool  # Whether the user should be referred to a lawyer
    civic_card: dict  # A formatted card for frontend display

class ComplianceResult(BaseModel):
    """
    Output schema for compliance checks.
    """
    is_compliant: bool
    is_unclear: bool
    suggested_remedies: List[str]
