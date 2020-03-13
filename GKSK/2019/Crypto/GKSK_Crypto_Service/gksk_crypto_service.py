#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import random
import base64

def banner():
    return '''

 Welcome to our brand new crypto service
   ________ _______ __ __    ____________  ______  __________     _____ __________ _    __________________
  / ____/ //_/ ___// //_/   / ____/ __ \ \/ / __ \/_  __/ __ \   / ___// ____/ __ \ |  / /  _/ ____/ ____/
 / / __/ ,<  \__ \/ ,<     / /   / /_/ /\  / /_/ / / / / / / /   \__ \/ __/ / /_/ / | / // // /   / __/
/ /_/ / /| |___/ / /| |   / /___/ _, _/ / / ____/ / / / /_/ /   ___/ / /___/ _, _/| |/ // // /___/ /___
\____/_/ |_/____/_/ |_|   \____/_/ |_| /_/_/     /_/  \____/   /____/_____/_/ |_| |___/___/\____/_____/
 version [v2.1.19]
    '''

def print_usage(script_argv):
    print '[==USAGE==]\n'
    print 'Encrypt File \t: %s -e [plaintext_file] [key]' % script_argv
    print 'Decrypt File \t: %s -d [encrypted_file] [key]' % script_argv
    print 'Generate Key \t: %s -g' % script_argv
    print 'Help \t\t: %s -h\n' % script_argv

def shift_key():
    key = random.randint(0x1, 0xff)
    return key

def shuffle_secret():
    secret_out = ''
    secret_str = ''.join('gksk-secret-code'.split('-'))
    for count,loop in enumerate(secret_str):
        if count % 2 == 0:
            secret_out += ''.join([chr(ord(ch) + 0x3) for ch in loop])
        else:
            secret_out += loop
    return secret_out

def encryption(plain, shift):
    try:
        ciphertext = ''
        length_msg = 50
        with open(plain, 'rb') as bin:
            data = bin.read()

        shift = int(shift)
        alphabet = shuffle_secret() * length_msg
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        for a, b in zip(data, shifted_alphabet):
            ciphertext += chr(ord(a) + ord(b) ^ shift)

        with open(plain + '.enc', 'wb') as bin:
            bin.write(base64.b64encode(ciphertext))

    except ValueError:
        print "ValueError : Range key [0-255]"
        exit()

def decryption(enc_file, key):
    with open(enc_file, 'rb') as bin:
        data = bin.read()

    '''NOT IMPLEMENTED YET'''

    with open(enc_file + '.trial', 'wb') as bin:
        bin.write(data)


def main():
    print banner()
    script_argv = sys.argv[0]
    try:
        mode = sys.argv[1]
        if mode == '-e':
            plaintext_file = sys.argv[2]
            key = sys.argv[3]
            encryption(plaintext_file, key)
            print "\nSECRET KEY : ", shuffle_secret()
            print '\nThankyou for using our service :)\n'
        elif mode == '-d':
            encrypted_file = sys.argv[2]
            key = sys.argv[3]
            decryption(encrypted_file, key)
            print '\nNot implemented yet. Upgrade to premium, only $99999\n'
        elif mode == '-g':
            print 'Key : ', shift_key()
        elif mode == '-h':
            print_usage(script_argv)
        else:
            print_usage(script_argv)
    except IndexError:
        print_usage(script_argv)

if __name__ == '__main__':
    main()
