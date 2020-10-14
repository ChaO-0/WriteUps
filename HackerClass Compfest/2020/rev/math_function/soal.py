

import numpy as np
import hashlib

data = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])
my_input = input()
password = np.array(list(map(ord, list(my_input[:4].ljust(4, '\x00')))))
result = list(np.matmul(data, password))
print(result)
if result == [7681, 4019, 7160, 8080]:
	print("Congratz, here is your flag: COMPFEST12{" + hashlib.sha384(bytes(my_input.encode())).hexdigest() + "}")

'''
import numpy as np

data = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])

res = np.array([7681, 4019, 7160, 8080])
array([7681, 4019, 7160, 8080])

datainv = np.linalg.inv(data)
np.dot(datainv, res)
'''