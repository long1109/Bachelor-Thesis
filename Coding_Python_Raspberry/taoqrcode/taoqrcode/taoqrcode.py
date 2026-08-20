import pyqrcode
import json
import math
import random

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
    

#config=ConfigParser()
#config.read('config.txt')
#ten=config.get('DEFAULT','ten')
#tuoi=config.get('DEFAULT','tuoi')
#key=config.get('DEFAULT','key')
#truong=config.get('DEFAULT','truong')
k='1234'
l=random.randint(1,10)
l1=str(l)
l2=k+l1
m={'idkhachhang':'1412103','idnhaxe':l2,'rsaidkhachhang':'','timestamp':''}#dang dict
n=json.dumps(m) #dang string
#qr_string='{}.{}.{}.{}.'.format(ten,tuoi,key,truong)
#q=pyqrcode.create(n)
long="123456789long123456"
q=pyqrcode.create(long)
q.png('myQR',scale=12)
print('QR Code generated...')


#print(l)
#print(l1)
#print(l2)

    

                    
