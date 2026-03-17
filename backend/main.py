from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Valor Shield backend is running 🚀"}