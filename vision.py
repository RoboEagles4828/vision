import socket
import time

import numpy as np
from imutils.video import FPS
import imutils

import camera
import cv2

# to setup ram disk
# in /etc/fstab add line "tmpfs /var/tmp tmpfs nodev,nosuid,size=50m 0 0"
# sudo mount -a

# initialize network socket
HOST = ''
PORT = 5800
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((HOST, PORT))
soc.listen(5)
conn, addr = soc.accept()
print("Got connection from", addr)

# initialize the video stream
stream = camera().start()
time.sleep(2.0)
fps = FPS().start()

# start cv loop
while True:
    # grab image from stream
    image = stream.read()
    image = imutils.resize(image, 320, 240)
    img = cv2.cvtColor(image, cv2.cv.CV_BGR2HSV)

    # do the stuff
    GREEN_MIN = np.array([50, 21, 156])
    GREEN_MAX = np.array([91, 181, 255])
    mask = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
    contours0, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
    contours1 = []
    # print cv2.contourArea(contours0[0])
    for cnt in contours0:
        # print(cnt)
        area = cv2.contourArea(cnt)
        print('area  = ' + str(area))

        if area > 100.0:
            contours1.append(cnt)
            print "hi"
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours1]
    xtotal = 0
    ytotal = 0
    # print contours
    if len(contours) > 0:
        a = max(contours, key=lambda x: cv2.contourArea(x))
        for i in a:
            xtotal += i[0][0]
            ytotal += i[0][1]
            xtotal /= len(a)
            ytotal /= len(a)

    # send to pi using network socket
    conn.send(str(xtotal) + "," + str(ytotal) + "\n")
    # print str(xtotal) + " " + str(ytotal)

    # save to ram disk
    cv2.imwrite("/var/temp/stream.jpg", image)

    # update the fps counter and print fps
    fps.update()
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
camera.stop()
