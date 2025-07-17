import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.lawyer_referral import refer_lawyer
from app.models.lawyer import ReferralRequest

def test_successful_referral():
    request = ReferralRequest(issue_type="Land", location="Kiambu")
    result = refer_lawyer(request)
    print("\n[SUCCESSFUL REFERRAL]")
    print(result.referral_card)
    assert result.success is True
    assert result.matched_lawyer.name == "Adv. Wanjiku N."

def test_unsuccessful_referral():
    request = ReferralRequest(issue_type="Tax", location="Marsabit")
    result = refer_lawyer(request)
    print("\n[UNSUCCESSFUL REFERRAL]")
    print(result.referral_card)
    assert result.success is False
    assert result.matched_lawyer is None

if __name__ == "__main__":
    test_successful_referral()
    test_unsuccessful_referral()