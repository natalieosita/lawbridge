import re
import json
from typing import List
from sentence_transformers import SentenceTransformer, util
from app.models.situation import ComplianceResult

# Load articles and model
with open("app/data/constitution.json", "r", encoding="utf-8") as f:
    ARTICLES = json.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')
ARTICLE_EMBEDS = [
    model.encode(article.get("title", "") + " " + article.get("text", ""), convert_to_tensor=True)
    for article in ARTICLES
]

# Sample rule set (you can move this to a separate file)
RULES = [
    {
        "pattern": r"\bdenied access\b",
        "verdict": "non-compliant",
        "article_number": 47,
        "title": "Fair Administrative Action",
        "summary": "Every person has the right to fair administrative action.",
        "remedies": ["File a complaint with the relevant authority.", "Request written justification."]
    },
    {
        "pattern": r"\bfreedom of expression\b",
        "verdict": "compliant",
        "article_number": 33,
        "title": "Freedom of Expression",
        "summary": "Every person has the right to freedom of expression.",
        "remedies": []
    }
]

def check_compliance(user_input: str, top_k: int = 1) -> ComplianceResult:
    """
    Checks compliance using rule-based and semantic methods.
    Returns a structured ComplianceResult.
    """
    # Rule-based check
    for rule in RULES:
        if re.search(rule["pattern"], user_input, re.IGNORECASE):
            verdict = rule["verdict"]
            if verdict == "compliant":
                return ComplianceResult(
                    is_compliant=True,
                    is_unclear=False,
                    suggested_remedies=[]
                )
            elif verdict == "non-compliant":
                return ComplianceResult(
                    is_compliant=False,
                    is_unclear=False,
                    suggested_remedies=rule.get("remedies", [])
                )

    # Semantic fallback
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = [util.pytorch_cos_sim(query_embedding, art_emb).item() for art_emb in ARTICLE_EMBEDS]
    top_idx = max(range(len(scores)), key=lambda i: scores[i])
    top_article = ARTICLES[top_idx]

    # Treat semantic matches as "unclear" for now
    return ComplianceResult(
        is_compliant=False,
        is_unclear=True,
        suggested_remedies=[]
    )