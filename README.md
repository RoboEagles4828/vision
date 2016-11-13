# vision
python + OpenCV on raspberry pi
## Setup
1. Rasberry Pi
    * `sudo raspi-config`
        * change hostname
        * increase gpu memory allocation
        * expand file system
    * mDNS
        * `sudo apt-get install libnss-mdns`
        * For mDNS support on windows, install [bonjour](https://support.apple.com/kb/DL999?locale=en_US) and unblock UDP port 5353 on your firewall.
2. OpenCV
    * Fast: Install from Package Managers
    ```
    sudo apt-get install python-pip python-dev
    sudo pip install numpy
    sudo apt-get install libopencv-dev python-opencv
    sudo apt-get install python-picamera
    sudo pip install imutils
    ```
    * Recommended: [Build OpenCV 3 From Source](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3)
