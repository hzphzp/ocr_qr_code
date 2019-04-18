from PIL import Image


class ChineseCharacter:

    def __init__(self, s: str, img: Image.Image, font: str):
        self.font = font.split(".")[0]  # 把后缀去掉
        data = s.split(" ")
        w, h = img.size
        self.value = data[0]
        self.x1, self.y2, self.x2, self.y1 = int(data[1]), h - int(data[2]), int(data[3]), h - int(data[4])
        self.image = img.crop((self.x1, self.y1, self.x2, self.y2))
        self.number = int(data[5])  # 这个是说明这个字符在第几张图片上

    def save(self):
        print(self.x1, self.y1, self.x2, self.y2)
        self.image.save("result/{}_{}.png".format(self.value, self.font))
