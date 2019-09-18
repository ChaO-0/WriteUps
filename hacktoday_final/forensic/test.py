import pytesseract
from PIL import Image
import glob

img_list = sorted(glob.glob("output/jpg/*.jpg"))
output = ""
for i in img_list:
	output += pytesseract.image_to_string(Image.open(i), config="-psm 10")

open("output.txt", "w+").write(output)
#print(output)
