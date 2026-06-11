from fastapi import FastAPI

app = FastAPI(title="BookShelf API")


@app.get("/")
def root():
    return {"message": "BookShelf API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
