import base64

secret_out = ''
secret_str = ''.join("gksk-secret-code".split("-"))
for count, loop in enumerate(secret_str):
	if count % 2 == 0:
		secret_out += ''.join([chr(ord(ch) + 0x3) for ch in loop])
	else:
		secret_out += loop

print secret_out

enc = open("flag.enc", "r").read()
shift_key = 0
while True:
	shift_key += 1
	cipher = base64.b64decode(enc)
	alphabet = secret_out * 50
	shifted_alphabet = alphabet[shift_key:] + alphabet[:shift_key]
	flag = ''
	for i in range(len(cipher[:-1])):
		flag += chr((ord(cipher[i]) ^ shift_key) - ord(shifted_alphabet[i]))

	if "GKSK{" in flag:
		print flag
		break
