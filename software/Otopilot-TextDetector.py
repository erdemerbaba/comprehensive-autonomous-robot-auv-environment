# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

a=pytesseract.image_to_string(Image.open('image.png'), lang="eng")

d=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","W","X",
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","w","x",
   "0","1","2","3","4","5","6","7","8","9"," ","  ","   ","    "]

for x in range(len(a)):
    for xx in range(len(d)):
        if a[x]==d[xx]:
            print(d[xx],end="")
