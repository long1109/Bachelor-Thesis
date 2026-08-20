import hashlib

s='1412103'
s1=hashlib.md5(s.encode('utf-8')).hexdigest()

print(s1)
