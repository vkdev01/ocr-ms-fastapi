# initialize fast api app

from fastapi import FastAPI

# for referencing requests
from fastapi import (
	Request,
	Depends,
	File,
	UploadFile,
	HTTPException
	)

# for return html responses
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import pathlib

# image verification
from PIL import Image

# Env Setup
from pydantic import BaseSettings
from functools import lru_cache
import io
import pathlib
import uuid

class Settings(BaseSettings):
	debug: bool = False
	echo_active: bool = False

	class Config:
		env_file = ".env"

@lru_cache
def get_settings():
	return Settings()

DEBUG = get_settings().debug


print(DEBUG)

# app setup
BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

@app.get("/", response_class=HTMLResponse) # http_get
def home_view():
	print(DEBUG)
	return "<h1>Hello World</h1>"


@app.get("/1", response_class=HTMLResponse) # http_get
# referencing requests on the view
def home_view(request : Request, settings:Settings = Depends(get_settings)):
	print(request)
	# context parameters
	params = {
		"request" : request, # key must be request
		"code" : "With Python"
	}
	return templates.TemplateResponse("home.html", params) # passing params is must

@app.post("/") # http_post
def home_view_post():
	return {"hello":"world"}



@app.post("/img-echo/", response_class=FileResponse) # http_post
async def img_echo_view(file: UploadFile = File(...), settings:Settings = Depends(get_settings)):
	if not settings.echo_active:
		raise HTTPException(detail="Invalid endpoint", status_code=400)


	UPLOAD_DIR.mkdir(exist_ok=True)

	# byte stream
	bytes_str = io.BytesIO(await file.read())

	try:
		img = Image.open(bytes_str)
	except:
		raise HTTPException(detail="Invalid image", status_code=400)


	fname = pathlib.Path(file.filename)
	fext = fname.suffix
	dest = UPLOAD_DIR / f"{uuid.uuid1()}-{fext}"

	img.save(dest)

	return dest
