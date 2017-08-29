from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = 'HD'
camera.rotation = 180
camera.start_preview()
sleep(30)
camera.stop_preview()
