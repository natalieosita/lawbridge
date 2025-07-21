# 📚 LawBridge — AI-Powered Legal Intelligence API + Full-Stack Platform

LawBridge is a multi-layered legal technology platform designed to democratize access to constitutional law in Kenya. At its core is a FastAPI-powered legal API that uses cutting-edge NLP to make the Constitution searchable, explainable, and understandable to everyday users. This is supported by a scalable MERN stack frontend that connects users with legal services, built for real-world hosting and seamless DevOps.

---

## 🚀 API Capabilities — LawBridge AI Legal Engine (FastAPI)

**🔌 Base URL**: `https://lawbridge-api.onrender.com`  
**📄 Docs**: [Interactive Swagger UI](https://lawbridge-api.onrender.com/docs)

### 🔍 Features

- **Semantic Article Search**  
  Find the most relevant constitutional articles using AI-powered language models.

- **AI-Powered Article Explanation**  
  Get simplified summaries of legal text tailored for students, citizens, policymakers, and professionals.

- **Constitutional Compliance Checker**  
  Evaluate if an action aligns with the Constitution—via rules and semantic interpretation.

- **Rights Finder**  
  Ask a natural language question and discover related rights and freedoms.

- **Legal Reference Links**  
  Each explanation may include connections to international law, statutes, and court cases.

### 📦 Endpoints Overview

| Method | Endpoint               | Description                                                   |
|--------|------------------------|---------------------------------------------------------------|
| GET    | `/search-article`      | Returns articles relevant to a legal query                    |
| GET    | `/explain-article-ai`  | AI-generated explanation with selectable tone                 |
| GET    | `/check-compliance`    | Checks if a described action is constitutionally compliant    |
| GET    | `/rights-finder`       | Discovers rights linked to natural language user input        |

> Full endpoint documentation available at `/docs`.

---

## 🧱 API Folder Structure

```plaintext
api/
└── app/
    ├── main.py                    # FastAPI entry point
    ├── routes/                    # API routes by feature
    │   ├── constitution.py
    │   ├── explainer_ai.py
    │   ├── compliance.py
    ├── services/                  # NLP logic and model interfaces
    │   ├── constitution_search.py
    │   ├── explainer_distilbart.py
    │   ├── compliance_engine.py
    ├── utils/                     # Formatters and helpers
    │   ├── card_formatter.py
    │   ├── reference_db.py
    └── data/                      # Legal corpus & model cache
        ├── constitution.json
        ├── explainer_cache.json
```

---

## 🧪 Local API Setup

```bash
# Clone the repo
git clone https://github.com/your-org/lawbridge.git
cd lawbridge/api

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload
```

> Requires Python 3.10 or 3.11 (some packages may not work with Python 3.13+)

Access locally: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 MERN Stack Interface (Client + Express)

LawBridge’s frontend and backend interface supports case registration, authentication, secure API calls, and responsive legal workflows. While the legal API powers intelligence, the MERN stack serves as the interaction layer.

### 🛠 Stack Summary

| Layer       | Technology                         |
|-------------|-------------------------------------|
| Frontend    | React + Styled-Components + React Router |
| Backend     | Express.js (Node.js)                |
| Database    | MongoDB Atlas                       |
| Auth        | JWT                                 |
| Hosting     | Vercel (frontend) + Render (backend)|
| Styling     | ThemeProvider, Dark/Light Switch    |
| CI/CD       | GitHub Actions                      |

### 📁 Folder Highlights

```plaintext
lawbridge/
├── client/        # React frontend
├── server/        # Express.js backend
├── api/           # FastAPI legal intelligence engine
├── .github/       # GitHub Actions workflows
└── README.md      # Combined documentation
```

---

## 🔧 Local Setup (Full Stack)

```bash
# Clone the repo
git clone https://github.com/your-org/lawbridge.git
cd lawbridge
```

### 🔹 Backend — Express.js

```bash
cd server
cp .env.example .env
npm install
npm run dev
```

### 🔹 Frontend — React

```bash
cd ../client
cp .env.local.example .env.local
npm install
npm start
```

### 🔹 API — FastAPI

```bash
cd ../api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🩺 Monitoring & CI/CD

| Tool        | Usage                                           |
|-------------|-------------------------------------------------|
| Render Logs | Monitor backend status                          |
| MongoDB Atlas | Track slow queries and CPU usage              |
| Sentry      | Full-stack error tracking                       |
| BetterStack | Health check uptime verification                |
| GitHub Actions | Automates deploy to Vercel and Render        |

---

## 🌒 Theme Support

- Light/Dark toggle via `styled-components`
- Auto-detect system theme
- Stored persistently in `localStorage`

---

## 🤝 Contributing & Acknowledgments

- Contributions welcome via pull requests and issues  
- Licensed under MIT  
- Powered by Kenya Law, HuggingFace Transformers, MongoDB, Vercel, and Render

---
