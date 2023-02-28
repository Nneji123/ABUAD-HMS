import cv2
import pytesseract
import numpy as np
import os
import re
from PIL import Image, ImageDraw, ImageFilter


blur_words = ['Beneficiary Account Number:', 'Beneficiary Name:', 'Bank:']

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('cv_1.png') 

image_text = pytesseract.image_to_string(image)

draw = ImageDraw.Draw(image)

boxes = pytesseract.image_to_boxes(image)

for box in boxes.splitlines():
    _, x1, y1, x2, y2, _ = box.split()
    draw.rectangle((int(x1), image.size[1]-int(y2), int(x2), image.size[1]-int(y1)), outline='red')

image.show()
