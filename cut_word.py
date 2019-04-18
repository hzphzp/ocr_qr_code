import pytesseract
from PIL import Image, ImageDraw
from my_class.Character import ChineseCharacter


def cut_word(img: Image.Image, font: str) -> list:
    img = img.resize((1000, 1000))
    draw = ImageDraw.Draw(img)
    w, h = img.size
    print(img.size)
    boxes = pytesseract.image_to_boxes(img, lang="chi_sim").split("\n")
    print(pytesseract.image_to_string(img, lang="chi_sim"))
    chars = []
    for b in boxes:
        char = ChineseCharacter(b, img, font)
        draw.rectangle([(char.x1, char.y1), (char.x2, char.y2)], outline="red")
    img.show()
    return chars


if __name__ == "__main__":
    img = Image.open("data/test4.png").convert("RGB")
    chars = cut_word(img)
    print(type(chars))
