import string

def sub_a68(a1):
    res = ''
    for i in a1:
        res += chr(ord(i) + 2)
    
    return res

def sub_9c7(a1):
    res = ''
    for i in a1:
        res += chr((ord(i) - 87) % 26 + 97) 
    
    return res

def solve():
    shits = string.lowercase + "_"
    for shit in shits:
        flag = shit  
        flag = sub_a68(flag)
        flag = sub_9c7(flag)
        print shit, " : ", hex(ord(flag))

if __name__ == "__main__":
    solve()