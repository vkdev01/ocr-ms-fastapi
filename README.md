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
uvicorn app.main:app --reload
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

------
SET these values in .env


```
import secrets
token = secrets.token_urlsafe(32)
```
put the generated token value in .env file

DEBUG = 1
ECHO_ACTIVE=1
APP_AUTH_TOKEN=
APP_AUTH_TOKEN_PROD=
SKIP_AUTH = 0
