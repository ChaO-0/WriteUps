import base64
from itertools import cycle


def encrypt(message, passphrase):
    ciphertext = bytes(a^b for a, b in zip(message.encode(), cycle(passphrase.encode())))
    return base64.b64encode(ciphertext).decode()


def decrypt(encrypted, passphrase):
    ciphertext = base64.b64decode(encrypted)
    return "".join(chr(a^b) for a, b in zip(ciphertext, cycle(passphrase.encode())))
