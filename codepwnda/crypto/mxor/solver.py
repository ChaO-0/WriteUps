import base64, string
from Crypto.Util.number import long_to_bytes
from pwn import sleep

def xors(msg, key):
	res = ''
	for i in range(len(msg)):
		res += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
	return res

def findKey():
    #known = str(int("flag{....}".encode('hex'), 16))
    #flag = open("test.enc", 'rb').read()
    known = str(int("codepwnda{.................................................}".encode('hex'), 16)) #bruteforce manual :v
    #harus cari len flag yg tepat biar dapet key
    flag = base64.b64decode(open("flag.enc", "rb").read())
    key = ''
    for i in range(len(known)):
        key += chr(ord(known[i]) ^ ord(flag[i]))
    return key[:5] #hint len key adalah 5

def decrypt():
    key = "hutan"
    flag = base64.b64decode(open("flag.enc", "rb").read())
    dec = ''
    for i in range(len(flag)):
        dec += chr(ord(flag[i]) ^ ord(key[i % len(key)]))
    return dec
# ----- TRIAL AND ERROR ------
#flag = "flag{test}"
#key = "xxa"
#m = str(int(flag.encode('hex'), 16))
#print m
#open("test.enc", "w+").write(xors(m, key))

key = findKey()
flag = decrypt()
#print hex(int(flag))[2:-1].decode('hex')
print "[+] Found key: " + key
print "[+] Decrypting"
sleep(1)
print "[+] Flag: " + long_to_bytes(flag)