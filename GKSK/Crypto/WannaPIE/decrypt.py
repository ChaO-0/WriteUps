#!/usr/bin/python3.7

import string, os, random, time, binascii
from Crypto.Cipher import AES

def generate_random(N):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

#ctime epoch got from epochconverter.com, convert it to timestamp 
#stat.info file gave me the change time
#random seed is from the change time
ctime_epoch = 1547459663
random.seed(ctime_epoch)
key, iv = generate_random(16), generate_random(16)

print("Key: {}".format(key))
print("iv: {}".format(iv))

enc_file = open("home/picture/another/1426487872207_DSC_0165-color_large.png.pie", "rb").read() 

aes = AES.new(key, AES.MODE_CBC, iv)
dec = aes.decrypt(enc_file)

data = open("1426487872207_DSC_0165-color_large.png", "wb").write(dec)
print("File Decrypted")