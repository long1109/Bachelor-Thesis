from picamera.array import PiRGBArray
from picamera import PiCamera
from pyzbar import pyzbar
import numpy as np
import argparse
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate=24
rawCapture= PiRGBArray(camera,size=(640, 480))
for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    image=frame.array
    cv2.imshow("ket qua",image)
    k=cv2.waitKey(5) & 0xFF
    rawCapture.truncate(0)
    if k== ord("q"):
        break
    
    
        
    
