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
import pyqrcode
import json
import mysql.connector
import random
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="test",
    database="testdb",
    )

my_cursor = mydb.cursor()
    
dnhaxe=8832188163324936600969684363469355244981196401824810640801524735202970664351#dung
#dnhaxe=8832188163324936600969684363469355244981196401824810640801524735202970664350
nnhaxe=37329697336905091329478204622674311479441632430026222105912859511619690965793
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate=24
rawCapture= PiRGBArray(camera,size=(640, 480))
barcodeData1=0
pin=18
pin1=23
pin2=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)

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
            print (barcodeData_string['type'])
            GPIO.output(pin,True)
            time.sleep(0.2)
            GPIO.output(pin,False)
            time.sleep(0.2)
            GPIO.output(pin,True)
            time.sleep(0.2)
            GPIO.output(pin,False)
            
            barcodeData1=barcodeData
            sql_select_query="""select * FROM users WHERE id = %s"""
            my_cursor.execute(sql_select_query,(barcodeData_string['idkhachhang'],))
            result = my_cursor.fetchall()
            for row in result:
                break
            e=int(row[2])
            n=int(row[3])
                
            s1=hashlib.md5(barcodeData_string['idkhachhang'].encode('utf-8')).hexdigest()
            k=bin(int(binascii.hexlify(s1.encode('utf-8')),16))
            k2=int(k,2)
            c1=int(barcodeData_string['rsaidkhachhang'])
            k1=pow(c1,e,n)
            #print(k1)
            k3=int(barcodeData_string['type'])
            k4 = 1
            if ((k1 == k2) and (k3 == 1)):## GUI XE
                
                ticksguixe=time.time()
                ticksguixe2=str(int(ticksguixe))
                ticksguixe3=hashlib.md5(ticksguixe2.encode('utf-8')).hexdigest()
                bam2=bin(int(binascii.hexlify(ticksguixe3.encode('utf-8')),16))
                bam3=int(bam2,2)
                ciphertext2=pow(bam3,dnhaxe,nnhaxe)
                ciphertext3=str(ciphertext2)
                
                #l=random.randint(1,10)
                #l1=str(l)#chuyen tu int ve str
                #l2=barcodeData_string['idkhachhang']+l1#random+id
                #print(type(l2))
                m={'idnhaxe':ticksguixe2,'rsaidnhaxe':ciphertext3}
                chuoiqr=json.dumps(m)
                q=pyqrcode.create(chuoiqr)
                q.png('myQR',scale=6)
                my_sql = """UPDATE users SET idnhaxe = %s WHERE id = %s"""
                my_cursor.execute(my_sql,(ticksguixe2,barcodeData_string['idkhachhang'],))
                mydb.commit()

                
                imgplot=plt.imshow(mpimg.imread("myQR"))
                plt.ion()
                plt.show()
                
                GPIO.output(pin1,True)
                plt.pause(0.001)
                time.sleep(20)#cho nay can co camera duoi xe#####
                GPIO.output(pin1,False)
                plt.close('all')
            elif ((k1 == k2) and (int(barcodeData_string['type']) == 2)):## TRA XE
                sql_select_query2="""select * FROM users WHERE id = %s"""
                my_cursor.execute(sql_select_query2,(barcodeData_string['idkhachhang'],))
                result1 = my_cursor.fetchall()
                for row1 in result1:
                    break
                
                l3=str(row1[5])
                l4=""
                if(l3 == barcodeData_string['idnhaxe']):
                     my_sql1 = """UPDATE users SET idnhaxe = %s WHERE id = %s"""
                     my_cursor.execute(my_sql1,(l4,barcodeData_string['idkhachhang'],))
                     mydb.commit()
                     GPIO.output(pin2,True)
                     time.sleep(20)
                     GPIO.output(pin2,False)
                else:
                    print("ma id nha xe sai")
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
