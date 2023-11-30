import hikvision.api
import numpy as np
import cv2 as cv
import time

# This will use http by default (not https)
# pass False to the digest_auth parameter of CreateDevice to fallback to basic auth
# (note that basic auth and http without ssl are inherently insecure)
# more recent hikvision firmwares default to turning basic auth off
# (and that's a good idea for security)
# hik_camera.enable_motion_detection()
# hik_camera.disable_motion_detection()
# hik_camera.is_motion_detection_enabled()

def hikvisionShowCamInfo(pwd, usr, ip):
    hik_camera = hikvision.api.CreateDevice(ip, username=usr, password=pwd)

    print("\n" + hik_camera.deviceinfo_url + "\n")



def showCam(usr, pwd, ip):
    # asking for password and username
    # cap = cv.VideoCapture('rtsp://'+ usr +':'+ pwd +'@' + ip + '/H264?ch=1&subtype=0')
    cap = cv.VideoCapture('Training\Video\Meme.mp4')
    # print('Accessed Camera at:'+ ip + '\n' + 'rtsp://'+ usr +':'+ pwd +'@' + ip + '/H264?ch=1&subtype=0')
    
    while(True):
        #print('About to start the Read command')
        ret, frame = cap.read()
        # median = cv.medianBlur(frame, 7)
        #print('About to show frame of Video.')
        cv.imshow("Capturing", frame)

        time.sleep(0.008)   # Delays for 5 seconds. You can also use a float value.
        #print('Running..')

        if cv.waitKey(1) & 0xFF == ord('q'):
            break



#Open and start a stream
def showstream(usrname, password, ip, hikinfo):
    showCam(usrname, password, ip)
    
    if hikinfo is True:
        hikvisionShowCamInfo(usrname, password, ip)
        
showCam(0,0,0)