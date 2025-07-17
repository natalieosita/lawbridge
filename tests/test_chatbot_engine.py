import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.services.chatbot_engine import handle_chat_turn

def test_explain_intent():
    user_input = "What does freedom of expression mean?"
    response = handle_chat_turn(user_input, intent="explain")
    print("\n[EXPLAIN INTENT]")
    print(response)

def test_rights_intent():
    user_input = "Do I have the right to protest?"
    response = handle_chat_turn(user_input, intent="rights")
    print("\n[RIGHTS INTENT]")
    print(response)

def test_assess_intent():
    user_input = "I was denied access to public records by a county officer."
    response = handle_chat_turn(user_input, intent="assess")
    print("\n[ASSESS INTENT]")
    print(response)

def test_search_intent():
    user_input = "administrative action"
    response = handle_chat_turn(user_input, intent="search")
    print("\n[SEARCH INTENT]")
    print(response)

def test_auto_intent():
    user_input = "My land was taken without compensation."
    response = handle_chat_turn(user_input, intent="auto")
    print("\n[AUTO INTENT]")
    print(response)

if __name__ == "__main__":
    test_explain_intent()
    test_rights_intent()
    test_assess_intent()
    test_search_intent()
    test_auto_intent()