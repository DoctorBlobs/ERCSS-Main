import cv2 as cv
import pathlib as pl
import numpy as np

def face_detect():
    face_cascade = cv.CascadeClassifier('Training/Cascade/data/haarcascade_frontalface_alt.xml')
    cap = cv.VideoCapture(0)
    
    while(True):
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # grays = []
        faces = face_cascade.detectMultiScale(
                                            gray, 
                                            scaleFactor=1.5, 
                                            minNeighbors=5,
                                            minSize=(30, 30)
                                            )
        
        for(x, y, w, h) in faces:
            print(x, y, w, h)
            roi_gray = gray[y:y+h, x:x+w] #Save gray image cut of the face
            roi_color = frame[y:y+h, x:x+w] #Save color image of face using coordinates
            
            img_item = "my-image.png"
            cv.imwrite(img_item, roi_gray)
            
            rectcolor = (255,0,0) #BGR
            stroke = 2
            end_x = x + w
            end_y = y + h
            cv.rectangle(frame, 
                        (x,y), 
                        (end_x, end_y), 
                        rectcolor, 
                        stroke)
            

            # for i in range(0, len(faces)):
            #     (x, y, w, h) = faces[i]
            #     grays.append(gray[y:y+w, x:x+h])
        
        #display frame
        cv.imshow('frame', frame)

        if cv.waitKey(20) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()     
            break     


face_detect()  



            
     

    