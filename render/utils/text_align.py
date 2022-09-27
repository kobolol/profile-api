from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_text_align(text, font, pic_size):
    ascent, descent = font.getmetrics()
    w = font.getmask(text).getbbox()[2]
    h = font.getmask(text).getbbox()[3] + descent

    h += int(h * 0.21)

    return (pic_size[0] - w) / 2, (pic_size[1] - h) / 2
