from fastapi import FastAPI

# Import all route modules
from app.routes.constitution import router as constitution_router
from app.routes.legal_bot import router as legal_bot_router
from app.routes.compliance import router as compliance_router
from app.routes.smart_compliance import router as smart_compliance_router
from app.routes.explainer_ai import router as explainer_ai_router
from app.routes.rights_finder import router as rights_finder_router
from app.routes.chat import router as chat_router  # ✅ New chatbot endpoint

# Create FastAPI app
app = FastAPI(title="LawBridge API")

# Register routers
app.include_router(constitution_router)
app.include_router(legal_bot_router)
app.include_router(compliance_router)
app.include_router(smart_compliance_router)
app.include_router(explainer_ai_router)
app.include_router(rights_finder_router)
app.include_router(chat_router)  # ✅ Chatbot integration