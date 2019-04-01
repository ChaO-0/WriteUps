from base64 import *

with open("1", "rb") as file:
    text = file.read()

decoded = ""


    decoded = b64decode(text)
    text = decoded

print text
 
