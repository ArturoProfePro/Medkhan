from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def _add_cors_middleware(app: FastAPI) -> None:
    """Add CORS Middleware."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*", "http://91.147.93.29:8000", "http://91.147.93.29"],
    )


def add_middleware(app: FastAPI) -> None:
    """Add all middlewares."""
    _add_cors_middleware(app)
