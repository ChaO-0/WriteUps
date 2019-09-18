import string

def rapiin():
  hai = """
        01h
        09h
        11h
        27h
        02h
        00h
        12h
        03h
        08h
        12h
        09h
        12h
        11h
        01h
        03h
        13h
        04h
        03h
        05h
        15h
        2Eh
        0Ah
        03h
        0Ah
        12h
        03h
        01h
        2Eh
        16h
        2Eh
        0Ah
        12h
        06h"""
  hai = hai.replace("\n", " ")
  hai = hai.replace("         ", " ")
  hai = hai.replace("h", "")
  hai = hai.replace(" ", " 0x")
  hai = hai.split(" ")
  return hai[1:]

def check(param_1):
  local_10 = 0
  key = "wf{_ny}xblrxxxxxxaeixotxxxxxxxxxxxxxxxxgxxxxxxu"
  while local_10 != -1 and ord(param_1) != ord(key[local_10]):
    if ord(param_1) < ord(key[local_10]):
      local_10 = local_10 * 2+ 1
    else:
      if ord(key[local_10]) < ord(param_1):
        local_10 = (local_10 + 1) * 2

  return local_10

def brute_force1():
  local_b0 = 0
  something = rapiin()
  newpos = []
  for i in something:
    newpos.append(int(i, 16))

  len_flag = 33
  printable = "wf{_ny}blraeiotgu"
  flag = "flag{xxxxxxxxxxxxxxxxxxxxxxxxxxx}"
  flag = list(flag)
  i = 0

  while local_b0 < 33:
    lvar2 = check(flag[local_b0])
    if lvar2 == newpos[local_b0]:
      #print "Benar", test[local_b0], lvar2
      local_b0 += 1
    else:
      #print "Salah", test[local_b0] , lvar2
      flag[local_b0] = printable[i]
      lvar2 = check(flag[local_b0])
      if(lvar2 == newpos[local_b0]):
        print ''.join(flag)
        i = 0
      else:
        i += 1

  flag = ''.join(flag)
  
  print "Found flag : {}".format(flag)

def brute_force2():
  local_b0 = 0
  something = rapiin()
  newpos = []
  for i in something:
    newpos.append(int(i, 16))

  len_flag = 33
  printable = "wf{_ny}blraeiotgu"
  flag = "flag{xxxxxxxxxxxxxxxxxxxxxxxxxxx}"
  flag = list(flag)
  i = 0
  while local_b0 < 33:
    try:
      lvar2 = check(flag[local_b0])
      if lvar2 == newpos[local_b0]:
        #print "Benar", test[local_b0], lvar2
        local_b0 += 1
      else:
        #print "Salah", test[local_b0] , lvar2
        flag[local_b0] = printable[i]
        lvar2 = check(flag[local_b0])
        if(lvar2 == newpos[local_b0]):
          print ''.join(flag)
          i = 0
        else:
          i += 1
    except IndexError:
      pass
  flag = ''.join(flag)
  print "Found flag : ", flag

if __name__ == "__main__":
  brute_force2()