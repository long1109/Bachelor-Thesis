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
    
dnhaxe=8524893698178839021842207513193574510686461035132126463158913416610373463797#dung
#dnhaxe=8832188163324936600969684363469355244981196401824810640801524735202970664350
nnhaxe=79710425938967830468396137237578837744486449057068804209709627857536329300881
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate=24
rawCapture= PiRGBArray(camera,size=(640, 480))
barcodeData1=0
pin=18
pin1=23
pin2=24
pin3=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image=frame.array
    barcodes=pyzbar.decode(image)
    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

        barcodeData=barcode.data.decode("us-ascii")
        barcodeType=barcode.type

        text="{}({})".format(barcodeData,barcodeType)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        
        if (barcodeData != barcodeData1):
            try:
                #
                mydb.commit()
                print (barcodeData)#dang string, tu string ko in dc key
                barcodeData_string= json.loads(barcodeData)#tu string chuyen ve dict
                print (barcodeData_string['idkhachhang'])#dang string
                print (barcodeData_string['idnhaxe'])
                #print (barcodeData_string['rsaidkhachhang'])
                print (barcodeData_string['timestamp'])
                print (barcodeData_string['type'])
            except:
                GPIO.output(pin3,True)
                time.sleep(2)
                GPIO.output(pin3,False)
                print("qr code ko hop le")
                barcodeData1=barcodeData
            else:
                
                
                
                
                #
                GPIO.output(pin,True)
                time.sleep(0.2)
                GPIO.output(pin,False)
                time.sleep(0.2)
                GPIO.output(pin,True)
                time.sleep(0.2)
                GPIO.output(pin,False)
                barcodeData1=barcodeData
                tickskiemtra=time.time()
                tickskiemtra2=int(tickskiemtra)
                print(tickskiemtra2)
                tickskiemtra3=int(barcodeData_string['timestamp'])#try except la time stamp tu android
                if ((tickskiemtra2 == tickskiemtra3+2) or (tickskiemtra2 == tickskiemtra3+3) or (tickskiemtra2 == tickskiemtra3+4) or (tickskiemtra2 == tickskiemtra3+5) or (tickskiemtra2 == tickskiemtra3+6) or (tickskiemtra2 == tickskiemtra3+1) or (tickskiemtra2 == tickskiemtra3)):
                    #
                    sql_select_query="""select * FROM users WHERE id = %s"""
                    my_cursor.execute(sql_select_query,(barcodeData_string['idkhachhang'],))
                    result = my_cursor.fetchall()
                    for row in result:
                        break
                    #
                    n=int(row[3])
                    e=int(row[2])
                    s1=hashlib.md5(barcodeData_string['idkhachhang'].encode('us-ascii')).hexdigest()
                    k=bin(int(binascii.hexlify(s1.encode('utf-8')),16))
                    k2=int(k,2)
                    c1=int(barcodeData_string['rsaidkhachhang'])
                    k1=pow(c1,e,n)
                    #print(k1)
                    k3=int(barcodeData_string['type'])
                    k4 = 1
                    if ((k1 == k2) and (k3 == 1)):## GUI XE
                        #
                        sql_select_query3="""select * FROM users WHERE id = %s"""
                        my_cursor.execute(sql_select_query,(barcodeData_string['idkhachhang'],))
                        result3 = my_cursor.fetchall()
                        for row3 in result3:
                            break
                        trangthai = int(row3[6])
                        if(trangthai == 0):
                            trangthai = 1
                            ticksguixe=time.time()
                            ticksguixe2=str(int(ticksguixe))
                            ticksguixe3=hashlib.md5(ticksguixe2.encode('us-ascii')).hexdigest()
                            bam2=bin(int(binascii.hexlify(ticksguixe3.encode('us-ascii')),16))
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
                            q.png('myQR',scale=3)
                            my_sql = """UPDATE users SET idnhaxe = %s WHERE id = %s"""
                            my_cursor.execute(my_sql,(ticksguixe2,barcodeData_string['idkhachhang'],))
                            my_sql2 = """UPDATE users SET trangthai = %s WHERE id = %s"""
                            my_cursor.execute(my_sql2,(trangthai,barcodeData_string['idkhachhang'],))
                            mydb.commit()
                            imgplot=plt.imshow(mpimg.imread("myQR"))
                            plt.ion()
                            plt.show()
                            GPIO.output(pin1,True)
                            plt.pause(0.001)
                            time.sleep(20)#cho nay can co camera duoi xe#####
                            GPIO.output(pin1,False)
                    
                            plt.close('all')
                        else:
                            print("xe da duoc gui")
                    elif ((k1 == k2) and (int(barcodeData_string['type']) == 2)):## TRA XE
                        sql_select_query2="""select * FROM users WHERE id = %s"""
                        my_cursor.execute(sql_select_query2,(barcodeData_string['idkhachhang'],))
                        result1 = my_cursor.fetchall()
                        for row1 in result1:
                            break
                        
                        #
                        l3=str(row1[5])
                        print("ma tu database" + l3)
                        mydb.commit()
                        l4=""
                        if(l3 == barcodeData_string['idnhaxe']):
                            #
                            my_sql1 = """UPDATE users SET idnhaxe = %s WHERE id = %s"""
                            my_cursor.execute(my_sql1,(l4,barcodeData_string['idkhachhang'],))
                            trangthai1 = 0
                            my_sql3 = """UPDATE users SET trangthai = %s WHERE id = %s"""
                            my_cursor.execute(my_sql3,(trangthai1,barcodeData_string['idkhachhang'],))
                            mydb.commit()
                            GPIO.output(pin2,True)
                            time.sleep(20)
                            GPIO.output(pin2,False)
                        else:#1
                            #
                            print("ma id nha xe sai")
                            GPIO.output(pin3,True)
                            time.sleep(2)
                            GPIO.output(pin3,False)
                            
                    else:#2
                        print("ma hoa sai id")
                        GPIO.output(pin3,True)
                        time.sleep(2)
                        GPIO.output(pin3,False)
                        
                        
                    
                else:
                    print("ma qr code qua han")
                    GPIO.output(pin3,True)
                    time.sleep(2)
                    GPIO.output(pin3,False)
                
            
        
         
                     
                                        
    cv2.imshow("ket qua",image)
    k=cv2.waitKey(5) & 0xFF
    rawCapture.truncate(0)
    if k== ord("q"):
        break
