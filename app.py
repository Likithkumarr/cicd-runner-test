from fastapi import FastAPI

app = FastAPI(title="CI/CD Test API", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "🎉 CI/CD Pipeline Deployed Automatically on Local Machine!",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
