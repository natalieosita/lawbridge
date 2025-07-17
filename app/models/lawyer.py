from pydantic import BaseModel
from typing import List, Optional

class ReferralRequest(BaseModel):
    issue_type: str
    location: str

class LawyerProfile(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    location: str
    specialties: List[str]
    verified: bool

class ReferralResult(BaseModel):
    matched_lawyer: Optional[LawyerProfile]
    referral_card: dict
    success: bool