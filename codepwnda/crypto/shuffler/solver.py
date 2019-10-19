import string
from pwn import sleep

def decrypt(msg):                         
    x = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    y = 'BXcjk7JCT5goWsq9Lhr2zvVISbKfGteauUHMlRiQ3Nd6A8p14OnmZ0xyYFPEwD'
    z = string.maketrans(x, y)
    return msg.translate(z)

if __name__ == "__main__":
    dt = open('ciphertext.txt').read().strip()
    pt = decrypt(dt)
    brute = 21
    while brute < 43:
        for _ in range(brute):                                              
            pt = decrypt(pt)
            if 'Cyber' in pt:
                print pt + '\n'
                break
        brute += 1 