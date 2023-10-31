import Camsystem as cs
import passwordsys as psys
import cv2 as cv
import pathlib as pl
import json

#cascadepath = pl.Path(cv.__file__).parent.absolute() / "Training"
    

def main():
    #Get Credentials
    credentials = psys.read_credentials()
    extracted_credentials = psys.extraction(credentials)
    
    print(credentials)
    
    camchoice = "camera_" + input("What Camera (Just input a number)")
    
    print(credentials[camchoice])
    
    usr = credentials[camchoice]
    pwd = credentials[camchoice]
    ip =  credentials[camchoice]
    cs.showstream(usr, pwd, ip, False)

main()
