from pwn import *
from base64 import b64decode
from Crypto.Util.number import long_to_bytes
import codecs
import json

p = remote("socket.cryptohack.org", 13377)

def solve():
    for i in range(0, 100):
        problem = p.recvline()
        problem = json.loads(problem)
        answer = ''
        if problem["type"] == 'base64':
            answer = b64decode(problem["encoded"])
        elif problem["type"] == 'hex':
            answer = problem["encoded"].decode('hex')
        elif problem["type"] == 'rot13':
            answer = codecs.decode(problem["encoded"], 'rot-13')
        elif problem["type"] == 'bigint':
            answer = long_to_bytes(int(problem["encoded"], 16))
        elif problem["type"] == 'utf-8':
            answer = ''.join([chr(x) for x in problem["encoded"]])
        answer = '{"decoded" : "%s"}' % answer
        print answer
        p.sendline(answer)

    p.interactive()
    

if __name__ == "__main__":
    solve()