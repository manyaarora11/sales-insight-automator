from fastapi import FastAPI, UploadFile, File
import pandas as pd
from ai_engine import generate_summary

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Insight Automator API running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    data = df.to_string()

    summary = generate_summary(data)

    return {
        "message": "File processed successfully",
        "summary": summary
    }