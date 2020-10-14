import string

def solve():
    alphabet = string.ascii_letters + string.digits + "~!@#$%^&*()_+-=`{}[]|\\;',./:\"<>?"
    secret = 'aQLpavpKQcCVpfcg'
    #(8 * input + 19) % 61 + 65 = secret

    flag = []

    for i in secret:
        for j in alphabet:
            if chr((8 * ord(j) + 19) % 61 + 65) == i:
                flag.append(j)
                break

    print ''.join(flag)

if __name__ == "__main__":
    solve()