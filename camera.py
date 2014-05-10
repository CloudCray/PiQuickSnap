import picamera

def take_photo(filename):
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	camera.capture(filename)
