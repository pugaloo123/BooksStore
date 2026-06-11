from fastapi import FastAPI
from .database import engine, Base
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
