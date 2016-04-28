import numpy as np
import cv2
#from time import clock
from numpy import pi, sin, cos
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import socket
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 15
camera.vflip = True
camera.hflip = True
camera.awb_mode = 'off'
#camera.image_effect = 'solarize'
#camera.image_effect_params = 0
camera.brightness = 75
camera.awb_gains = (1.45,1.45)
camera.exposure_mode = 'off'
rawCapture = PiRGBArray(camera, size=(320, 240))

#initialize network socket
HOST = ''
PORT = 5800
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((HOST, PORT))
soc.listen(5)
conn,addr = soc.accept()
print ("Got connection from",addr)

# allow the camera to warmup
time.sleep(1.0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	#do the stuff
 	img= cv2.resize(image,(320,240))
	img2=cv2.cvtColor(img, cv2.cv.CV_BGR2HSV)
	#GREEN_MIN=np.array([58,28,138])
	#GREEN_MAX=np.array([96,255,255])
	GREEN_MIN=np.array([57,0,156])
        GREEN_MAX=np.array([91,181,255])
	mask = cv2.inRange(img2, GREEN_MIN, GREEN_MAX)
	contours0, hierarchy = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours1=[]
	#print cv2.contourArea(contours0[0])
	for cnt in contours0:
		#print(cnt)
		M = cv2.moments(cnt)
		#print(M['m00'])
		#area=cv2.contourArea(cnt)
		area = M['m00']
		"""
		hull = cv2.convexHull(cnt)
		hull_area = cv2.contourArea(hull)
		try:
			solidity = float(area)/hull_area
			break
		except ZeroDivisionError:
			#print('hull = ' + str(hull_area))
			solidity = 74
		"""
    		print('area  = ' + str(area))
		#print solidity
    		if area>100.0: # and solidity<75:
        		contours1.append(cnt)
			print "hi"
	contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours1]
	xtotal=0
	ytotal=0
	#print contours
	if len(contours)>0:
		a= max(contours,key= lambda x: cv2.contourArea(x))
		for i in a:
    			xtotal+=i[0][0]
    			ytotal+=i[0][1]
			xtotal/=len(a)
			ytotal/=len(a)
	print str(xtotal) + " " + str(ytotal)
	#send to pi using network socket
       	conn.send(str(xtotal) + "," + str(ytotal) + "\n")
	#these are the coordinates we want to aim at. Now get them on the PI!!!
	# clear the stream in preparation for the next frame
	#cv2.imwrite("/home/pi/tostream/stream.jpg", image)
	rawCapture.truncate(0)
camera.close()
