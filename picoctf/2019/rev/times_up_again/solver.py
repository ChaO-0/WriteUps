from pwn import *

def solve():
    p = process("./times-up-again")
    p.recvuntil("Challenge: ")
    chall = p.recvuntil("S")
    chall = chall[:-2]
    pram = eval(chall)
    pram = str(pram)
    p.sendline(pram)

    p.interactive()

if __name__ == "__main__":
    solve()