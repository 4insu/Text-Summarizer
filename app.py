"""

from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
import PyPDF2
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text: str = None, pdf_file: UploadFile = File(None)):
    try:
        if pdf_file:
            pdf_text = extract_text_from_pdf(pdf_file)
            obj = PredictionPipeline()
            summary = obj.predict(pdf_text)
        elif text:
            obj = PredictionPipeline()
            summary = obj.predict(text)
        else:
            return Response("No input provided")

        return Response(content=summary, media_type="text/plain")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.file as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text.encode('latin-1', 'replace').decode('latin-1')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)


"""

from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from textSummarizer.pipeline.prediction import PredictionPipeline
import PyPDF2
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

@app.get("/", response_class=HTMLResponse, tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def predict_form(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request, "message": ""})

@app.post("/predict", response_class=HTMLResponse)
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

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file.file as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text.encode('latin-1', 'replace').decode('latin-1')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)