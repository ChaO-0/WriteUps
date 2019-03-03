from base64 import *

enc = "XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH"
flag = b64decode(enc)
key = ":)"
newflag = []
for i, l in enumerate(flag):
	kunci = ord(key[i % len(key)])
	cipher = ord(l)
	newflag.append(chr(kunci ^ cipher))

newflag = ''.join(newflag)
print newflag
