import base64, string

def xors(msg, key):
	res = ''
	for i in range(len(msg)):
		res += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
	return res

flag = "KCTF{Crypt0_itU_Sus4h_k4lo_g4k_b1S4_MAt3MAt1kA}"
key = "tzu"
#assert len(key) == 5 and all(x in string.lowercase for x in key)

m = str(int(flag.encode('hex'), 16))
c = xors(m, key)
open('flag', 'w+').write(base64.b64encode(c))
