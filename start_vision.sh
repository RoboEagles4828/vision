#!/bin/bash
until python /home/pi/vision/vision.py; do
    sleep 1
done
