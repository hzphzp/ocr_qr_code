import config
from PIL import Image
import cut_word
import os

font_list = [config.FONT_NAME_Micro, config.FONT_NAME_HuaWen]
for font in font_list:
    cut_word.cut_word_with_size_and_border.count = 0
    path = "data/{}/".format(font)
    files = os.listdir(path)
    for f in files:
        print(f)
        img = Image.open(path + f)
        img = img.resize(config.IMAGE_SIZE)
        # img.show()
        chars_list = cut_word.cut_word_with_size_and_border(img, font)
