import picamera

camera = picamera.PiCamera()

def take_photo(filename):
	camera.resolution = (640,480)
	camera.capture(filename)
