#!/bin/bash

#start streamer
/home/pi/vision/start_mjpg_streamer.sh

#restart vision script when client breaks connection
until python /home/pi/vision/vision.py; do
    sleep 1
done
