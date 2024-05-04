from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummary.pipeline.prediction import PredictionPipeline

text:str = "What is Text Sumaarization"

app = FastAPI(

)
@app.get("Overview", tags = ["Text Summary"])
async def index():
    return RedirectResponse(url="/docs")

@app.post("Predictions")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        return e


if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0",port=8080)
