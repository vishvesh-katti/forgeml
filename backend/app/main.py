from fastapi import FastAPI

app = FastAPI(
    title="ForgeML API",
    description="Enterprise AI & Machine Learning Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "ForgeML API Running 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }