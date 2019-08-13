from base64 import *
with open("base", "r") as file:
    text = file.read()
    decoded = ""
    while True:
        decoded = b64decode(text)
        text = decoded
        if(text.find("CTF{") != -1):
           break
    print text
