from cut_word import cut_word
from PIL import Image
from pretreat import pretreat
import read_chinese
from generator import generator_iter

# Definition of some constant
FONT_Sun = "SimSun.ttf"

chars = read_chinese.read_chinese3000()
generator_iter(chars)
'''
img = Image.open("data/test_pic.jpg").convert("RGB")
img = pretreat(img)
chars = cut_word(img, FONT_Sun)
'''