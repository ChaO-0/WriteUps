from pyzbar.pyzbar import decode
from PIL import Image
import glob

files = glob.glob("hachi/*.jpg")
blog = ""

for i in files:
    decoded = str(decode(Image.open(i))[0][0])
    blog += decoded + "\n"

open("flagHachi.txt", "w+").write(blog)

# print(files)