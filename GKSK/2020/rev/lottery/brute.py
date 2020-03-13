from random import randint
import string
FLAG = 'R E D A C T E D'

def prime():
    prime = []
    for Number in range(1, 51):
        count = 0
        for i in range(2, Number // 2 + 1):
            if Number % i == 0:
                count = count + 1
                break

        if count == 0 and Number != 1:
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
        elif i % 6 == 0 and i not in prime():
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
            if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1
        elif i % 3 == 0 and i not in prime():
            if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                prob += 1
        elif 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
            prob += 1

    if prob < 10:
        return prob
    if 10 <= prob <= 25:
        return prob
    if 25 < prob <= 40:
        return prob
    if 40 < prob <= 49:
        return prob
    if prob == 50:
        return 'You got FLAG: {}'.format(FLAG)


def main():
    letters = string.ascii_letters + string.digits + "~`!@#$%^&*()_+-={}[];:'\"\\/?.>,<"
    for i in range(len(letters)):
        print(letters[i], check("Z000a6n0a0g9i7aqu0a0q000ZgZ0a0U0u0ugU0AAg0a0ag00aX")

if __name__ == '__main__':
    main()