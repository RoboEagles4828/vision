from imutils.video.pivideostream import PiVideoStream


class camera(PiVideoStream):
    def __init__(self):
        PiVideoStream.__init__(self, (640, 480))
        # camera.vflip = True
        camera.hflip = True
        camera.awb_mode = 'off'
        # camera.image_effect = 'solarize'
        # camera.image_effect_params = 0
        camera.brightness = 75
        camera.awb_gains = (1.45, 1.45)
        camera.exposure_mode = 'off'
