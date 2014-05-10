from datetime import datetime
import upload
import camera

from button import *

upload.ACCESS_TOKEN = upload.new_access_token()

def upload_photo():
	timestamp = datetime.now().isoformat().replace("T","_")
	fn = "/home/pi/photos/" + timestamp + ".jpg"
	camera.take_photo(fn)
	ui = upload.upload_image(fn, title=timestamp)
	print(fn + " - " + ui.link)

camera.camera.start_preview()

# GPIO.add_event_detect(23, GPIO.RISING, callback=upload_photo, bouncetime=50)
while True:
	GPIO.wait_for_edge(23, GPIO.FALLING)
	upload_photo()
GPIO.cleanup()
