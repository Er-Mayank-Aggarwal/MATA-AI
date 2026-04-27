from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.routes.question_routes import router
from app.middleware.error_handler import global_exception_handler, validation_exception_handler
from app.config import get_settings

settings = get_settings()

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="CBSE Question Generator API",
    description="AI-powered CBSE question generator for Class 9 & 10 — Maths, Science, Social Science",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Middleware
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router)

# Static Files (Frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.on_event("startup")
async def startup_event():
    key_peek = f"{settings.groq_api_key[:4]}...{settings.groq_api_key[-4:]}" if settings.groq_api_key else "MISSING"
    print(f"--- API STARTUP ---")
    print(f"Model: {settings.groq_model}")
    print(f"Key:   {key_peek}")
    print(f"Env:   {settings.env}")
    print(f"-------------------")


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "CBSE Question Generator API is running"}


@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy", "model": settings.groq_model}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.port, reload=True)