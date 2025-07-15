from fastapi import APIRouter, Query
from app.services.compliance_engine import check_compliance

router = APIRouter()

@router.get("/check-compliance")
def compliance_check(action: str = Query(..., description="Describe the action to check for constitutional compliance")):
    """
    Check if a given action is compliant with the constitution.
    """
    return check_compliance(action)