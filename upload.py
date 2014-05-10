import os
import pyimgur

from my_settings import CLIENT_ID

def upload_image(filename, title=None):
	im = pyimgur.Imgur(CLIENT_ID)
	uploaded_image = im.upload_image(filename, title)
	return uploaded_image


