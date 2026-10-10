from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="AI Incident & Log Analysis Assistant")

class LogRequest(BaseModel):
    log_text: str
    api_key: str

@app.post("/analyze")
async def analyze_log(request: LogRequest):
    if not request.log_text.strip():
        raise HTTPException(status_code=400, detail="Log text cannot be empty.")
    
    try:
        client = OpenAI(api_key=request.api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI Incident Response Specialist. Analyze system logs and provide a structured report with: 1. Summary of Issue 2. Likely Root Cause 3. Recommended Remediation Steps."},
                {"role": "user", "content": f"Logs:\n{request.log_text}"}
            ]
        )
        return {"status": "success", "analysis": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
