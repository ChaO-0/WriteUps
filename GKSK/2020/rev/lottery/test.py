# uncompyle6 version 3.5.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Aug  7 2019, 00:51:29) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
# Embedded file name: uler.py
# Compiled at: 2020-03-03 01:44:07
# Size of source mod 2**32: 3338 bytes
import string
from random import randint
FLAG = 'R E D A C T E D'

def banner():
    print('\n+=======================================================+\n|                                                       |\n|    .____           __    __                           |\n|    |    |    _____/  |__/  |_  ___________ ___.__.    |\n|    |    |   /  _ \\   __\\   __\\/ __ \\_  __ <   |  |    |\n|    |    |__(  <_> )  |  |  | \\  ___/|  | \\/\\___  |    |\n|    |_______ \\____/|__|  |__|  \\___  >__|   / ____|    |\n|            \\/                     \\/       \\/         |\n|                                                       |\n+=======================================================+\n')


def prime():
    prime = []
    for Number in range(1, 51):
        count = 0
        for i in range(2, Number // 2 + 1):
            if Number % i == 0:
                count = count + 1
                break

        if count == 0:
            if Number != 1:
                prime.append(Number)

    return prime


def check(ticket):
    ticket = list(ticket)
    if len(ticket) != 50:
        return 'Invalid ticket...'
    prob = 0
    for i in range(50):
        if i in prime():
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
        else:
            if i % 6 == 0:
                pass
            if i not in prime():
                if 65 <= ord(ticket[i]) - 20 <= 90:
                    prob += 1
            elif i % 5 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                    prob += 1
            elif i % 9 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) <= 57:
                    prob += 1
            elif i % 13 == 0 and i not in prime():
                if 65 <= ord(ticket[i]) <= 90:
                    prob += 1
            elif i % 4 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122:
                    if ord(ticket[i]) % 10 == 7:
                        prob += 1
            elif i % 3 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                    prob += 1
            elif 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1
    return prob

if __name__ == "__main__":
    letters = string.ascii_letters + string.digits
    # for i in range(len(letters)):
        # print "Loop {} with char '{}'".format(i, letters[i])
    print check("ZZ00Z7Z7YXZ1Z7ZXZ7Z9ZZZ7ZZZZZ9Z9ZZZZZ6ZZY9Z7ZZZ6ZZ")