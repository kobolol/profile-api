from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from render.utils.text_align import get_text_align
import os


def render_worker(name: str, theme: int, themes, THIS_FOLDER:str):
    img = Image.open(os.path.join(THIS_FOLDER, f"render/themes/{themes[theme].getdataname()}"))
    font = ImageFont.truetype(os.path.join(THIS_FOLDER, f"render/fonts/{themes[theme].getfontname()}"), int(themes[theme].getbold()))

    draw = ImageDraw.Draw(img)

    msg = name

    draw.text(get_text_align(msg, font, (1024, 1024)), msg, (int(themes[theme].getcolor1()), int(themes[theme].getcolor2()), int(themes[theme].getcolor3())), font=font)
    img.save(os.path.join(THIS_FOLDER, f"render/outputs/{name}{theme}.png"))
    return os.path.join(THIS_FOLDER, f"render/outputs/{name}{theme}.png")
