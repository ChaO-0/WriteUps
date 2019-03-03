# Python2 ver.
# If you use Python3 interpreter, the trouble will be in print format

# [KSL Playground][Crypto][IDCC2018 DecryptME] written by Mr. Goodnight
# Link: https://euectf.stikom-bali.ac.id/challenges#[IDCC]%20DecryptME
# Flag: IDCC{S1mpl3_4nd_stR4ight}

from base64 import *

# Encryption algorithm
# ciphertext = plaintext + keys
with open('./enkripsi', mode = 'r') as f:
	ciphertext = f.read()

# plaintext = ciphertext - keys
# Make my own function to decrypt the ciphertext
def decrypt(ciphertext, keys):
	plaintext = ""
	for num,char in enumerate (ciphertext):
		plaintext += chr((ord(char) - ord(keys[num % len(keys)])) % 127)
			
	return plaintext

# keys = ciphertext - plaitext
# Find the key by using known string attack 
# Then I found out that the key is raja
known_string = b64encode("IDCC{")
keys = ""
for num,char in enumerate (known_string):
	keys += chr((ord(ciphertext[num]) - ord(char)) % 127)

# Run the decrypt function the decode it
keys = "raja"
flag = b64decode(decrypt(ciphertext, keys))
print ("Flag: {f}".format(f = flag))
