
import codecs
#convert hex to base64
#str object is already unicode object
s=input("enter the hex string")
b=codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()
print (b)
