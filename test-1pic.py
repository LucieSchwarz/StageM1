import time
import picamera

camera = picamera.PiCamera()
camera.exif_tags['IFD0.Artist']='pi2-00'
camera.rotation = 0 # in degree
camera.resolution = (640,480)


try :
    # camera.start_preview()
    time.sleep(1) # in second
    camera.capture('q.jpg')
    # camera.capture('imageTest.jpg', resize=(320, 240))
    # camera.stop_preview()
finally :
    camera.close()
    
