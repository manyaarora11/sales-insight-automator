import smtplib
from email.mime.text import MIMEText
import os
from fastapi import FastAPI, UploadFile, File
import pandas as pd
from ai_engine import generate_summary
def send_email(summary, recipient):

    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    msg = MIMEText(summary)
    msg["Subject"] = "Sales Insight Summary"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Insight Automator API running"}

@app.post("/upload")
async def upload_file(file: UploadFile, email: str):

    content = await file.read()
    data = content.decode()

    summary = generate_summary(data)

    send_email(summary, email)

    return {"message": "Summary generated and email sent"}