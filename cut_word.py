import pytesseract
from PIL import Image, ImageDraw
from my_class.Character import ChineseCharacter


def cut_word(pth: str) -> list:
    img = Image.open(pth).convert("RGB")
    img = img.resize((1000, 1000))
    draw = ImageDraw.Draw(img)
    w, h = img.size
    print(img.size)
    boxes = pytesseract.image_to_boxes(img, lang="chi_sim").split("\n")
    chars = []
    for b in boxes:
        char = ChineseCharacter(b, img)
        draw.rectangle([(char.x1, char.y1), (char.x2, char.y2)], outline="red")
    img.show()
    return chars


if __name__ == "__main__":
    chars = cut_word("data/test3.png")
    print(type(chars))
