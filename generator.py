from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import read_chinese


# Definition of some constant
DOC_DIM = (20, 20)
BOARDER_SIZE = 2
FONT_SIZE = 200
FOREGROUND_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_Sun = "SimSun.ttf"


def generator(chars: str, font_name: str, size: int) -> Image.Image:
    IMAGE_SIZE = (size*DOC_DIM[0] + 2*BOARDER_SIZE, size*DOC_DIM[1] + 2*BOARDER_SIZE)
    img = Image.new("RGB", IMAGE_SIZE, FOREGROUND_COLOR)
    font = ImageFont.truetype(font_name, size)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (IMAGE_SIZE[0]-1, IMAGE_SIZE[1]-1)], FOREGROUND_COLOR, BACKGROUND_COLOR)
    try:
        for row in range(DOC_DIM[1]):
            for col in range(DOC_DIM[0]):
                draw.text((BOARDER_SIZE + col*size, BOARDER_SIZE + row*size), chars[row*DOC_DIM[0]+col], BACKGROUND_COLOR, font=font)
    except IndexError:
        pass
    return img


def generator_iter(chars):
    chars_list = []
    x = 0
    number = DOC_DIM[0] * DOC_DIM[1]
    while number * x + number < len(chars):
        chars_list.append(chars[number * x: number * x + number])
        x += 1
    for chars_i in chars_list:
        img = generator(chars_i, "data/fonts/{}".format(FONT_Sun), 40)
        # img.show()
        img = np.array(img)
        cv2.imshow("", img)
        cv2.waitKey(0)


if __name__ == "__main__":
    chars = read_chinese.read_chinese3000()
    generator_iter(chars)
