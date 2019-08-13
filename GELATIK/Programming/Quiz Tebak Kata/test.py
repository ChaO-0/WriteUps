from pwn import *                                                
from PIL import Image                                            
import pytesseract
import base64                                       
                                                                 
r = remote('180.250.7.183', 7007)                                
                                                                 
def stringToRGB(data):
    obj = Image.open(io.BytesIO(data)).convert("RGB")
    obj_rotate = obj.transpose(Image.FLIP_LEFT_RIGHT)
    obj_rotate.save('image.png')
    return pytesseract.image_to_string(Image.open('image.png'))

for i in range(20):
    r.recvuntil('berikut:\n')
    enc = r.recvline().decode('utf-8')
    data = stringToRGB(base64.b64decode(enc))
    r.recvuntil('detik')
    r.sendline(str(data))

print(str(data)) 
print(r.recv().decode('utf-8')) 
