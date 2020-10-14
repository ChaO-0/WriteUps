import hashlib

horses = open("horse_names.txt", "rb").read().split('\r\n')[:-1]
for horse in horses:
    print hashlib.md5(("Horse_" + horse).encode()).hexdigest()

print hashlib.md5(("Horse_MechaOmkar-YG6BPRJM").encode()).hexdigest()
