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

# ⚖️ LawBridge MERN Stack Overview
LawBridge’s frontend and backend interface supports case registration, authentication, secure API calls, and responsive legal workflows. While the legal API powers intelligence, the MERN stack serves as the interaction layer.

## 🚀 Tech Stack Overview

| Layer       | Technology                          |
|-------------|--------------------------------------|
| Frontend    | React (JSX), React Query, Axios      |
| Styling     | Styled-Components, ThemeProvider     |
| Backend     | Express.js, Node.js                  |
| Database    | MongoDB Atlas                        |
| Auth        | JWT                                  |
| Deployment  | Vercel (client) + Render (server)    |
| DevOps      | GitHub Actions (CI/CD)               |
| Monitoring  | Render Healthchecks, Sentry-ready    |
| Testing     | Jest, Supertest, Testing Library     |

---

## 🗂️ Folder Structure

```
lawbridge/
├── client/
│   ├── src/
│   │   ├── api/          # Axios client & React Query hooks
│   │   ├── components/   # UI components & Theme toggle
│   │   ├── pages/        # Routed views
│   │   ├── styles/       # global.js, theme.js
│   │   ├── utils/        # token/auth helpers
│   │   └── __tests__/    # Frontend unit tests
│   ├── public/           # Static assets
│   └── vercel.json       # Vercel config
│
├── server/
│   ├── controllers/      # Logic per route
│   ├── models/           # MongoDB schemas
│   ├── routes/           # Express endpoints
│   ├── middleware/       # Auth, validation
│   ├── tests/            # Backend test suite
│   └── render.yaml       # Render deployment config
│
└── .github/
    └── workflows/        # CI/CD pipelines
```

---

## 📚 Features

- 🔐 JWT Authentication & Protected Routes
- 🎨 Light/Dark Mode Toggle (Header)
- 💾 Theme Persistence via `localStorage`
- 🧠 System Theme Detection (`matchMedia`)
- 🚦 Health Check Endpoint (`/health`)
- ⚡ React Query + Axios Data Fetching
- 🧪 Test Scaffolding (frontend/backend)
- 🛠 CI/CD: GitHub Actions → Vercel & Render
- 📑 Deployment-Ready Environment Handling
- 🌍 Responsive Design

---

## 🧠 Technical Architecture

```text
                      ┌──────────────┐
                      │ MongoDB Atlas│
                      └─────┬────────┘
                            │
                     ┌──────▼───────┐
                     │ Express Server│
                     │ /auth /cases  │
                     └──────┬────────┘
                            │ JWT
                            ▼
┌────────────────────────────────────────────────────────┐
│ React Frontend (Vercel)                                │
│ - Protected Routes: /dashboard, /cases                 │
│ - Theme Toggle + System Detection                      │
│ - Axios + React Query integration                      │
│ - Styled Components w/ ThemeProvider                   │
└────────────────────────────────────────────────────────┘
```

---

## 🧰 Setup Instructions

### 🖥 Local Dev

```bash
git clone https://github.com/your-org/lawbridge.git

# Backend
cd server
cp .env.example .env
npm install
npm run dev

# Frontend
cd ../client
cp .env.local.example .env.local
npm install
npm start
```

### 🔐 `.env` Files

#### `client/.env.local`

```env
REACT_APP_API_URL=https://lawbridge-api.onrender.com
```

#### `server/.env`

```env
MONGO_URI=your-mongodb-uri
JWT_SECRET=your-secret
PORT=5000
NODE_ENV=production
```

---

## 🧪 Testing

### ✅ Frontend: `__tests__/`

- `Header.test.js`: checks navigation rendering
- Use Jest + @testing-library/react

### ✅ Backend: `tests/`

- `auth.test.js`: register/login flow
- Use Jest + Supertest

Run with:

```bash
npm test
```

---

## 🌐 API Reference

| Method | Endpoint           | Description              | Auth |
|--------|--------------------|--------------------------|------|
| POST   | `/auth/register`   | Create new user          | ❌   |
| POST   | `/auth/login`      | Login existing user      | ❌   |
| GET    | `/cases`           | Retrieve user cases      | ✅   |
| POST   | `/cases`           | Submit new case          | ✅   |
| GET    | `/health`          | Check server status      | ❌   |

---

## 🧭 Deployment Strategy

### ✅ Vercel (Frontend)

- Root: `client/`
- `vercel.json`:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "framework": "create-react-app"
}
```

### ✅ Render (Backend)

- Uses `render.yaml`
- Health check: `/health`

### 🤖 GitHub Actions

- On push to `client/` → Trigger Vercel
- On push to `server/` → Trigger Render

```yaml
# frontend.yml
run: curl -X POST ${{ secrets.VERCEL_DEPLOY_HOOK }}

# backend.yml
run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

---

## 📜 User Guide

1. Visit `https://lawbridge-6n006rrhp-natalieositas-projects.vercel.app/`
2. Register and login
3. Access dashboard and submit cases
4. Use theme toggle to switch UI appearance
5. All data persists and is securely transmitted via JWT

---

## 📄 License & Attribution

This project is open-source for educational and portfolio purposes.  
Please credit LawBridge in any redistributed work.
