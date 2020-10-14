from pwn import * 

password = "Z#P#Y\xb9ZmT[$D5\x06[c@[xAd\xf0{(i.UxCA`j"
# p = process("./angrmanagement")
p = remote("challenges.tamuctf.com", 4322)
p.sendline(password)
p.interactive()