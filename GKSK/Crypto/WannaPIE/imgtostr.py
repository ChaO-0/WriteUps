from PIL import Image
import pytesseract

def readFlag():
    data1 = pytesseract.image_to_string(Image.open('img/realflagpart1.png'))
    data2 = pytesseract.image_to_string(Image.open('img/realflagpart2.png'))
    print(data1)
    print(data2)
    
if __name__ == "__main__":
    readFlag()
