from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from textSummarizer.pipeline.prediction import PredictionPipeline
import uvicorn
import PyPDF2
import os

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

# Mounting static files for CSS, JavaScript, etc.
app.mount("/assets", StaticFiles(directory = "templates/assets"), name = "assets")

# Endpoint to render the index.html template
@app.get("/", response_class = HTMLResponse, tags = ["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint to render the form for prediction
@app.get("/predict", response_class = HTMLResponse)
async def predict_form(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request, "message": ""})

# Endpoint to handle prediction request
@app.post("/predict", response_class = HTMLResponse)
async def predict_route(request: Request, input_type: str = Form(...), text: str = Form(None), pdf_file: UploadFile = File(None)):
    try:
        if input_type == "pdf" and pdf_file:
            pdf_text = extract_text_from_pdf(pdf_file)
            obj = PredictionPipeline()
            summary = obj.predict(pdf_text)
        elif input_type == "text" and text:
            obj = PredictionPipeline()
            summary = obj.predict(text)
        else:
            return templates.TemplateResponse("predict.html", {"request": request, "message": "Invalid input or no input provided"})

        return templates.TemplateResponse("predict.html", {"request": request, "summary": summary})
    except Exception as e:
        return templates.TemplateResponse("predict.html", {"request": request, "message": f"Error Occurred! {e}"})

# Function to extract text from uploaded PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.file as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text.encode('latin-1', 'replace').decode('latin-1')

if __name__ == "__main__":
    # Running the FastAPI app using Uvicorn server
    uvicorn.run(app, host = "0.0.0.0", port = 8000)