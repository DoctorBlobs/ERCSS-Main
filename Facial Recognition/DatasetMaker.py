import cv2 as cv
import pathlib as pl
import numpy as np
import os

face_id = input('\n enter user id end press enter')

def face_recognition(imgpath, max_files):
    face_cascade = cv.CascadeClassifier('Training/Cascade/data/haarcascade_frontalface_alt.xml')
    cap = cv.VideoCapture(0)
    
    count = 0
    
    while(True):
        
        files = os.listdir(imgpath)
        
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

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
            
            count += 1
                        
            rectcolor = (255,0,0) #BGR
            stroke = 2
            end_x = x + w
            end_y = y + h
            cv.rectangle(frame, 
                        (x,y), 
                        (end_x, end_y), 
                        rectcolor, 
                        stroke)
            

            
            if len(files) <= max_files:
                cv.imwrite(imgpath + str(face_id) + '-' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                cv.imshow('image', frame)
            else:
                print(f"Folder '{imgpath}' is full.")
                break



        if cv.waitKey(20) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()     
            break     





def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")






folder_path = "D:/Coding/Languages/Python/Projects/ERCSS-Main/Training/Dataset/" + face_id + "/"  # Change this to the desired folder name
max_files_allowed = 100

create_folder_if_not_exists(folder_path)
face_recognition(folder_path, max_files_allowed)



            
     

    