import base64
a=raw_input()
b=base64.b64encode(a.decode('hex'))
print b
