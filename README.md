# ocr-tool
A simple OCR tool made using FastAPI and PyTesseract.

## Setup
```
brew install tesseract
pip install -r requirements.txt
```

## Starting a local server
```
cd src
uvicorn server:app --reload
```


Here's a list of the packages we will use to accomplish this:

- FastAPI
- Tesseract OCR
- pytesseract
- pre-commit
- pytest
- Gunicorn
- Uvicorn
- Requests
