"""

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

"""


import streamlit as st
import PyPDF2
import speech_recognition as sr
from textSummarizer.pipeline.prediction import PredictionPipeline

# Function to capture audio and convert it to text
def audio_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        st.write("Toggle the checkbox to start/stop speaking.")
        while st.session_state['listening']:
            audio = r.listen(source, phrase_time_limit = 100)  # Set the maximum recording time to 10 seconds (adjust as needed)
            try:
                text = r.recognize_google(audio)
                st.write("You said:", text)
                summarizer = PredictionPipeline()
                summary = summarizer.predict(text)
                st.write("Summary:", summary)
            except sr.UnknownValueError:
                st.error("Sorry, I could not understand what you said.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Function to extract text from uploaded PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_number in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_number].extract_text()
    return text.encode('latin-1', 'replace').decode('latin-1')

def main():
    img_path = "images/logo_1.png"
    st.sidebar.image(img_path, use_column_width = True)

    st.sidebar.title("Text Summarizer")

    # Sidebar for input selection
    input_type = st.sidebar.radio("Navigation", ("Text", "PDF", "Voice"))

    if input_type == "Text":
        st.title("Summarize Text")

        text_input = st.text_area("Enter Text:")
        if st.button("Summarize"):
            if text_input:
                summarizer = PredictionPipeline()
                summary = summarizer.predict(text_input)
                st.write("Summary:", summary)
            else:
                st.error("Please enter some text.")
    elif input_type == "PDF":
        st.title("Summarize PDF")

        pdf_file = st.file_uploader("Upload PDF File:", type=["pdf"])
        if st.button("Summarize"):
            if pdf_file is not None:
                pdf_text = extract_text_from_pdf(pdf_file)
                summarizer = PredictionPipeline()
                summary = summarizer.predict(pdf_text)
                st.write("Summary:", summary)
            else:
                st.error("Please upload a PDF file.")
    elif input_type == "Voice":
        st.title("Summarize Audio")

        st.write("Toggle the checkbox to start/stop speaking.")
        st.session_state['listening'] = st.checkbox("Start/Stop Speaking")
        if st.session_state['listening']:
            audio_to_text()

if __name__ == "__main__":
    main()
