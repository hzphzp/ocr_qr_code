from PIL import Image
import numpy as np


def pretreat(img: Image.Image):
    img_data = np.array(img)
    img_data = np.mean(img_data, -1)  # 将rgb转为灰度图
    # 二值化
    img_data[img_data > 50] = 255

    img_data[img_data <= 50] = 0
    img = Image.fromarray(img_data)
    return img


    


