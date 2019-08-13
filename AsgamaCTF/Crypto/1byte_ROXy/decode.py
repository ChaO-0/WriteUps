from pwn import *

cipher = "e7c1cdc1e3f4e6dbcfcec5ffc2d9d4c5ffd8cfd2d29f9fdd"

cipher = cipher.decode('hex')

for i in range(256):
	plain = xor(cipher, i)
	if "GamaCTF{" in plain:
		print plain
		break

