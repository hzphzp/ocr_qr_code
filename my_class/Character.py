class ChineseCharacter:

    def __init__(self, s: str):
        data = s.split(" ")
        self.value = data[0]
        self.location = [int(x) for x in data[1: 5]]
        self.number = int(data[5])  # 这个是说明这个字符在第几张图片上

