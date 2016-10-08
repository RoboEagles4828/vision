#!/bin/bash

#start mjpg-streamer
#env LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH mjpg_streamer -o "output_http.so -w ./www -p 1180" -i "input_raspicam.so -fps 15  -x 320 -y 240 -rot 180 -br 50 -ex off -awb off"

env LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH mjpg_streamer -o "output_http.so -w ./www -p 1180" -i "input_file.so -f /home/pi/tostream"
