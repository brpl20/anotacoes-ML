import cv2
import json
import pytesseract

img = cv2.imread('cpf-test.jpg')
text = pytesseract.image_to_string(img)
print(text)
