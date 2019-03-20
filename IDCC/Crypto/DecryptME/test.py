from base64 import *
def enkripsi(plain, keys):
	enc = []
	plain = b64encode(plain)
	for i, l in enumerate(plain):
		kunci = ord(keys[i % len(keys)])
		teks = ord(l)
		enc.append(chr((teks + kunci) % 127))
                #enc = teks + kunci
	return ''.join(enc)

def findKey():
    key = []
    known = b64encode("IDCC{")
    file = open("enkripsi", "rb")
    file = file.read()
    for i, l in enumerate(known):
        enc = ord(file[i])
        teks = ord(l)
        key.append((chr((enc - teks) % 127)))
    return ''.join(key)

def decryption():
    key = "raja"
    flag = []
    file = open("enkripsi", "r").read()
    for i, l in enumerate(file):
        kunci = ord(key[i % len(key)])
	cipher = ord(l)
	flag.append(chr((cipher - kunci) % 127))
    return ''.join(flag)

    
print findKey()
print b64decode(decryption())
