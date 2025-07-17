# LawBridge API

LawBridge is a FastAPI-powered API that makes the Constitution of Kenya accessible, searchable, and understandable for everyone. It uses state-of-the-art NLP models to answer legal questions, explain constitutional articles in plain language, and provide relevant legal references.

---

## Features

- **Semantic Article Search:**  
  Find the most relevant constitutional articles for any legal question using advanced language models.

- **AI-Powered Article Explanation:**  
  Get plain-language or audience-specific summaries of constitutional articles (student, civic, policy, formal, or neutral tone).

- **Compliance Checker:**  
  Check if an action is compliant with the Constitution using both rule-based and semantic search methods.

- **Rights Finder:**  
  Discover your rights by querying the Constitution in natural language.

- **Legal References:**  
  Each response can include references to international law, statutes, and case law for deeper context.

---

## API Endpoints

- `GET /search-article`  
  Search for relevant constitutional articles by query.

- `GET /explain-article-ai`  
  Get an AI-generated explanation of a constitutional article in a specified tone.

- `GET /check-compliance`  
  Check if an action is constitutionally compliant.

- `GET /rights-finder`  
  Find rights and freedoms related to your query.

- ...and more (see `/docs` for full API documentation).

---

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/Currybroketherecord/lawbridge.git
   cd lawbridge
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure you have Python 3.10 or 3.11**  
   (Some dependencies may not work with Python 3.13+)

4. **Run the API**
   ```sh
   uvicorn app.main:app --reload
   ```

5. **Open your browser at**  
   [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation.

---

## Project Structure

```
app/
  main.py
  routes/
    constitution.py
    explainer_ai.py
    compliance.py
    ...
  services/
    constitution_search.py
    explainer_distilbart.py
    compliance_engine.py
    ...
  utils/
    card_formatter.py
    reference_db.py
    ...
  data/
    constitution.json
    explainer_cache.json
    ...
```

---

## Data Sources

- **Constitution of Kenya** (official PDF, parsed to JSON)
- **Legal references** (international law, statutes, case law) in `reference_db.py`

---

## Contributing

Pull requests and issues are welcome!  
Please open an issue for feature requests or bug reports.

---

## License

This project is open source and available under the MIT License.

---

## Acknowledgments

- [Kenya Law](https://www.kenyalaw.org/)
- [HuggingFace Transformers](https://huggingface.co/)
-
