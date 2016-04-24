import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 15
camera.vflip = True
camera.hflip = True
camera.awb_mode = 'off'
#camera.image_effect = 'colorbalance'
#camera.image_effect_params = 0
camera.brightness = 60
camera.awb_gains = (1.5,1.5)
camera.exposure_mode = 'off'
#camera.saturation = 50
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(1.0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	cv2.imwrite("/home/pi/tostream/stream.jpg", image)
	rawCapture.truncate(0)
camera.close()
