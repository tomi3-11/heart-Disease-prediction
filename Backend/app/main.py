from fastapi import FastAPI

app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "API is running"}
