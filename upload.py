import os
import pyimgur

from my_settings import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, REFRESH_TOKEN

def upload_image(filename, title=None):
	im = pyimgur.Imgur(CLIENT_ID, 
			client_secret=CLIENT_SECRET,
			access_token=ACCESS_TOKEN, 
			refresh_token=REFRESH_TOKEN)
	uploaded_image = im.upload_image(filename, title)
	return uploaded_image


#  from authorize import new_access_token
