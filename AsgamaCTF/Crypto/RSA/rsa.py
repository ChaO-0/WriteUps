from pwn import *
from Crypto.Util.number import *

n = """00:95:44:59:90:95:cc:79:7b:a2:52:7c:0c:82:7c:
    aa:4a:3f:57:cb:e0:9a:b6:8b:0c:75:3c:4b:d3"""

n = n.replace(":", "")
n = n.replace("\n", "")
n = n.replace(" ", "")

n = int(n, 16)
e = 65537
c = int(open("enc_flag", "rb").read())
p = 3852454912858673504993326758109153
q = 4080423863932134851980426919817779
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
#print hex(m)[2:].decode('hex')
log.info("Public Key = {}".format(n))
log.info("Private Key = {}".format(d))
log.info("Ciphertext = {}".format(c))
log.info("Plaintext = {}".format(long_to_bytes(m)))
