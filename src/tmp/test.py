import pytesseract
from PIL import Image
image = Image.open("../songti.png")
boxes = pytesseract.image_to_boxes(image, lang="chi_sim")
pytesseract.image_to_string(image, lang="chi_sim")
boxes = boxes.split("\n")


