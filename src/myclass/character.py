class character:

    def __init__(self, s: str):
        data = str.split(" ")
        self.value = data[0]
        self.location = data[1: 5]
        self.number = data[5]  # 这个是说明这个字符在第几张图片上

