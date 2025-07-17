from app.services.explainer_distilbart import explain_article_distilbart
from app.services.constitution_search import search_constitution
from app.services.situation_assessor import assess_situation
from app.services.rights_finder import find_rights
from app.utils.card_formatter import format_explainer_card
from app.models.situation import SituationInput
from app.services.lawyer_referral import refer_lawyer
from app.models.lawyer import ReferralRequest

def handle_chat_turn(user_input: str, intent: str = "auto") -> dict:
    """
    Handle a single chatbot turn.
    Routes input to the appropriate service based on intent.
    """
    # Step 1: Intent routing
    if intent == "explain":
        article = search_constitution(user_input)[0]  # Top match
        explanation = explain_article_distilbart(article["article_number"], tone="civic")
        return format_explainer_card(explanation)

    elif intent == "rights":
        rights_card = find_rights(user_input)
        return rights_card  # Already formatted

    elif intent == "assess":
        situation = SituationInput(description=user_input)
        result = assess_situation(situation)
        return result.civic_card

    elif intent == "search":
        articles = search_constitution(user_input)
        return {
            "cardType": "searchResults",
            "query": user_input,
            "results": articles[:3]  # Top 3 matches
        }

    elif intent == "refer":
    # Example: "I need a lawyer for land issues in Kiambu"
    # You can later extract these from NLP or structured input
       request = ReferralRequest(issue_type="Land", location="Kiambu")
       result = refer_lawyer(request)
       return result.referral_card
    else:
        # Default fallback: treat as situation assessment
        situation = SituationInput(description=user_input)
        result = assess_situation(situation)
        return result.civic_card