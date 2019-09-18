from pwn import *

r = remote("35.185.187.162", 17001)

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
flag = "^FBi\*PpUDA-\,[l`.1qTUPg`.10_QgcckJ^]VQ_cP0tZd6_TWRaQU5_[Dc2VS';"
save = []

print string[41:52]

for i in range(len(string)):
	r.sendlineafter(": ", "hacktoday{who_needs_wizard_if_u_pro_at_analyze}"+ string[i])
	r.recvuntil("basebox :")
	print i , ": " + string[i] + ": "+ r.recv()
	#save.append(r.recv())
'''
n = 0
for i in save:
	print n, ": ", i
	n += 1
'''
