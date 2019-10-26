from PIL import Image
import pytesseract

im = Image.open("img1.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')
print(text)
