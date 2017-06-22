import time
import picamera

camera = picamera.PiCamera()

camera.resolution = (640,480)
#640*480 --->160ko/u et 29fps
#1280*720 -->485ko/u et 26fps
#1920*1080 -->1mo/u et 19fps
#2592*1944 -->1.7mo/u et 9fps

camera.rotation = 0 # in degree
camera.exif_tags['IFD0.Artist']='pi2-00'
nbOfImages = 10

try :
    camera.start_preview()
    time.sleep(10) #in second
    start=time.time()
    camera.capture_sequence(
        ('image%03d.jpg' % i
         for i in range(nbOfImages)
         ),
        use_video_port=True
        )
    # resize option can be used. with camera.capture
    
    print("Captured",nbOfImages,"images at %.2ffps" % (nbOfImages / (time.time()
-start)))    
    camera.stop_preview()
finally :
    camera.close()
    
