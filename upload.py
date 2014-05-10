import os
import pyimgur

CLIENT_ID = os.environ["IMGUR_API"]

def upload_image(filename, title=None):
	im = pyimgur.Imgur(CLIENT_ID)
	uploaded_image = im.upload_image(filename, title)
	return uploaded_image


