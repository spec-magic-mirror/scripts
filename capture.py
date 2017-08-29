import picamera
import time
import datetime

with picamera.PiCamera() as camera:
	camera.resolution = (2592, 1944)
	camera.rotation = 180
	camera.exposure_compensation = 5
	camera.start_preview()
	time.sleep(3)
	ts = time.time()
	tstring = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S'))
	camera.capture("./samples/" + tstring + ".jpg")
