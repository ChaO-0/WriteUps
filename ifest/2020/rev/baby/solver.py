enc = [0xB3, 0x60, 0x1F, 0x98, 0x4E, 0xB4, 0x8C, 0xDD, 0xB1, 0xB5, 
  0xF0, 0x28, 0xB2, 0x65, 0x1A, 0xE6, 0xC6, 0xC9, 0x22, 0x8D, 
  0x36, 0x45, 0xC4, 0x03, 0x0B, 0x0A, 0xB8, 0xF4, 0x06, 0xB4, 
  0x82, 0x43, 0x8C, 0xB5, 0xF0, 0xA7, 0xA2, 0x28, 0xA0, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00]
key = [0xFA, 0x26, 0x5A, 0xCB, 0x1A, 0xCF, 0xDE, 0xEE, 0xC7, 0xD0, 
  0x82, 0x5B, 0xD7, 0x3A, 0x7F, 0xD5, 0xFF, 0xF8, 0x4C, 0xBE, 
  0x05, 0x37, 0xF5, 0x6D, 0x6C, 0x55, 0xDE, 0xC4, 0x74, 0xEB, 
  0xE0, 0x77, 0xEE, 0xCC, 0xAF, 0xDE, 0xC7, 0x4D, 0xDD]

flag = ''
for i in range(len(enc)):
    flag += chr(enc[i] ^ key[i % len(key)])

print flag