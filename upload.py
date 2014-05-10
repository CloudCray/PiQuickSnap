import os
import pyimgur
import json

import sys

from my_settings import CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, REFRESH_TOKEN

if sys.version_info[0] < 3:
	import urllib2 as request
	import urllib as parse
else:
	import urllib.request as request
	import urllib.parse as parse

def new_access_token():
	url = "https://api.imgur.com/oauth2/token"
	req = request.Request(url)
	params = {
		"refresh_token": REFRESH_TOKEN,
		"client_id": CLIENT_ID,
		"client_secret": CLIENT_SECRET,
		"grant_type": "refresh_token"
	}
	req.add_data(parse.urlencode(params).encode("utf-8"))
	resp = request.urlopen(req)
	resp_text = resp.read().decode("ascii")
	resp_dict = json.loads(resp_text)
	new_token = resp_dict["access_token"]
	return new_token


def upload_image(filename, title=None):
	im = pyimgur.Imgur(CLIENT_ID, 
			client_secret=CLIENT_SECRET,
			access_token=ACCESS_TOKEN, 
			refresh_token=REFRESH_TOKEN)
	uploaded_image = im.upload_image(filename, title=title)
	return uploaded_image



