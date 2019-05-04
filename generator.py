import config
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import read_chinese


def generate_doc(chars: str, font_name: str):
    print(font_name)
    img = Image.new("RGB", config.DOC_IMAGE_SIZE, config.FOREGROUND_COLOR)
    font = ImageFont.truetype(font_name, config.FONT_SIZE)
    draw = ImageDraw.Draw(img)
    draw.rectangle(
        xy=[(config.BLANK_SIZE[0], config.BLANK_SIZE[1]), (config.DOC_IMAGE_SIZE[0] - config.BLANK_SIZE[0], config.DOC_IMAGE_SIZE[1] - config.BLANK_SIZE[1])],
        outline=config.BACKGROUND_COLOR,
        width=config.BOARDER_SIZE)
    try:
        cursor = 0
        for row in range(1, config.DOC_DIM[1] - 1):
            for col in range(1, config.DOC_DIM[0] - 1):
                draw.text(
                    (config.BLANK_SIZE[0] + config.BOARDER_SIZE + col * (config.FONT_SIZE + 2 * config.MARGIN_SIZE)
                     + config.MARGIN_SIZE, 
                     config.BLANK_SIZE[1] + config.BOARDER_SIZE + row * (config.FONT_SIZE + 2 * config.MARGIN_SIZE)
                     + config.MARGIN_SIZE), chars[cursor], config.BACKGROUND_COLOR,
                    font=font)
                cursor += 1
    except IndexError:
        pass
    return img


def generate_iter(chars: str, font_name: str):
    font_name = "data/fonts/{}.ttf".format(font_name)
    for i in range(0, len(chars), config.DOC_DIM[0] * config.DOC_DIM[1]):
        image = generate_doc(chars[i:], font_name)
        #     display(generate_doc(chars[i:], "fonts/{}".format(FONT_NAME), FONT_SIZE))
        img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        cv2.imshow("img", img)
        cv2.waitKey()


if __name__ == "__main__":

    # 生成文档，敲回车生成下一页
    chars = read_chinese.read_chinese3500()
    # generate_doc(chars, config.FONT_NAME_Fangzheng)
    generate_iter(chars, config.FONT_NAME_HuaWen)
