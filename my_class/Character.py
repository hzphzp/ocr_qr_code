from PIL import Image


class ChineseCharacter:

    def __init__(self, s: str, img: Image.Image):
        data = s.split(" ")
        w, h = img.size
        self.value = data[0]
        self.x1, self.y2, self.x2, self.y1 = int(data[1]), h - int(data[2]), int(data[3]), h - int(data[4])
        self.image = img.crop((self.x1, self.y1, self.x2, self.y2))
        self.number = int(data[5])  # 这个是说明这个字符在第几张图片上

    def save(self, pth: str):
        filename = pth + self.value + ".png"
        print(filename)
        self.image.save(filename)
        print(self.x1, self.y1, self.x2, self.y2)
