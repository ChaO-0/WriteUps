#!/usr/bin/env python3

import base64,numpy

def keyCheck(key):
    if not (0 < len(key) < 5):
        print("ERROR: key length min. 1 char and max. 4 char")
        exit()
    for i in range(len(key)):
        if not (65 <= ord(key[i]) <= 90):
            print("ERROR: capital letter only")
            exit()
    key = list(key)
    matrix = []
    counter = 0
    for i in range(2):
        temp = []
        for j in range(2):
            temp.append(ord(key[counter%len(key)]))
            counter += 1
        matrix.append(temp)
    
    if(not (numpy.linalg.det(matrix)) ):
        print("ERROR: singular matrix")
        exit()
    
    return matrix
    
def textToMatrix(text):
    text = text.strip()
    text = list(text)
    matrix = []
    while True:
        if len(text)%2 != 0:
            text.append(" ")
        else:
            break
    counter= 0
    for i in range(len(text)//2):
        temp = []
        for j in range(counter,counter+2):
            temp.append(ord(text[counter]))
            counter += 1
        matrix.append(temp)
    return matrix

def matrixToText(matrix):
    cipher = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = chr(matrix[i][j])
        cipher += ''.join(matrix[i])
    return base64.b64encode(str.encode(cipher)).decode('utf-8')

def encrypt(plaintext,key):
    ciphertext = []
    for x in range(len(plaintext)):
        row = []
        for y in range(len(key[0])):
            total = 0
            for z in range(len(key)):
                total = total + (plaintext[x][z] * key[z][y])
            row.append(total)
        ciphertext.append(row)
    return ciphertext

def main():
    
    plaintext = input("plaintext: ")
    key = input("key: ")

    plaintext = textToMatrix(plaintext)
    keyMatrix = keyCheck(key)
    ciphertext = encrypt(plaintext,keyMatrix)
    ciphertext = matrixToText(ciphertext)
    print("ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
