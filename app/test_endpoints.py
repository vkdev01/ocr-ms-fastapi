from app.main import app, BASE_DIR, UPLOAD_DIR # importing app object from main module

# needed for testing
from fastapi.testclient import TestClient

import shutil
import time
from PIL import Image, ImageChops
import io


client = TestClient(app) # Testing client for app
"""
Similiar to requests
r = requests.get()
"""

def test_get_home():
	response = client.get("/")
	assert response.status_code == 200
	assert "text/html" in response.headers['content-type']
	assert response.text != "<p>random</p>"




def test_post_home():
	response = client.post("/")
	assert response.status_code == 200
	assert "application/json" in response.headers['content-type']
	assert response.json() == {"hello" : "world"}



# valid_image_extensions = ['png', 'jpeg', 'jpg']


def test_echo_upload():
	sample_images_path = BASE_DIR / "images"

	for path in sample_images_path.glob('*'):

		try:
			img = Image.open(path)
		except:
			img = None


		response = client.post("/img-echo/", files={'file' : open(path, 'rb')})


		if img is None:
			assert response.status_code == 400
		else:
			# returning a valid image
			assert response.status_code == 200
			r_stream = io.BytesIO(response.content)
			echo_imge = Image.open(r_stream)
			difference = ImageChops.difference(echo_imge, img).getbbox()
			assert difference is None


	time.sleep(5)
	shutil.rmtree(UPLOAD_DIR)
