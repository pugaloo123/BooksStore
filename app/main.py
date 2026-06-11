from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from .database import engine, Base, SessionLocal
from .routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BookShelf API")

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "BookShelf API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"status": "ready"}
