import pytesseract

from PIL import Image
from my_class.Character import ChineseCharacter
import numpy as np

image = Image.open("/home/huangzp/code/ocr_qr_code/data/songti.png")
boxes = pytesseract.image_to_boxes(image, lang="chi_sim")
pytesseract.image_to_string(image, lang="chi_sim")
boxes = boxes.split("\n")
chars = []
c_images = []

image = np.array(image)
for c in boxes:
    chars.append(ChineseCharacter(c))

for c in chars:
    x1, y1 = c.location[0], c.location[1]
    x2, y2 = c.location[2], c.location[3]
    print(x1, x2, y1, y2)
    c_image = image[x1: x2, y1: y2]
    c_image = Image.fromarray(c_image)
    c_image.show()
    c_image.save(c.value + ".png")




