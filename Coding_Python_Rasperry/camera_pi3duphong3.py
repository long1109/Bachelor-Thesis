from picamera.array import PiRGBArray
from picamera import PiCamera
from imutils.video import VideoStream
from pyzbar import pyzbar
import numpy as np
import json
import cv2
import RPi.GPIO as GPIO
import time
import hashlib
import math
import binascii
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

e=281692188811534932411700825886972443691
n=61585782000322565211213027396251628256519876094144898656255590243791531617141
#n=61585782000322565211213027396251628256519876094144898656255590243791531617140
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate=24
rawCapture= PiRGBArray(camera,size=(640, 480))
barcodeData1=0
pin=18
pin1=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image=frame.array
    barcodes=pyzbar.decode(image)
    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

        barcodeData=barcode.data.decode("utf-8")
        barcodeType=barcode.type

        text="{}({})".format(barcodeData,barcodeType)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        
        if (barcodeData != barcodeData1):
            print (barcodeData)#dang string, tu string ko in dc key
            barcodeData_string= json.loads(barcodeData)#tu string chuyen ve dict
            print (barcodeData_string['idkhachhang'])#dang string
            print (barcodeData_string['idnhaxe'])
            print (barcodeData_string['rsaidkhachhang'])
            print (barcodeData_string['timestamp'])
            GPIO.output(pin,True)
            time.sleep(0.2)
            GPIO.output(pin,False)
            time.sleep(0.2)
            GPIO.output(pin,True)
            time.sleep(0.2)
            GPIO.output(pin,False)
            time.sleep(0.2)
            barcodeData1=barcodeData
            s1=hashlib.md5(barcodeData_string['idkhachhang'].encode('utf-8')).hexdigest()
            k=bin(int(binascii.hexlify(s1.encode('utf-8')),16))
            k2=int(k,2)
            c1=int(barcodeData_string['rsaidkhachhang'])
            k1=pow(c1,e,n)
            print(k1)
            if (k1 == k2):
                imgplot=plt.imshow(mpimg.imread("myQR"))
                plt.ion()
                plt.show()
                
                GPIO.output(pin1,True)
                plt.pause(0.001)
                time.sleep(5)
                GPIO.output(pin1,False)
                plt.close('all')
            else:
                print("ma hoa sai id")
            
            


        
            
            #if (barcodeData_string['idkhachhang'] == '1412103'):
             #   GPIO.output(pin1,True)
              #  time.sleep(5)
               # GPIO.output(pin1,False)
                
               
                
                
        #print(barcodeData[0])
        
        
        
                                        
    cv2.imshow("ket qua",image)
    k=cv2.waitKey(5) & 0xFF
    rawCapture.truncate(0)
    if k== ord("q"):
        break
