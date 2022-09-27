from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from render.utils.text_align import get_text_align


def render_worker(name: str, theme: int, themes):
    img = Image.open(f"render/themes/{themes[theme].getdataname()}")
    font = ImageFont.truetype(f"render/fonts/{themes[theme].getfontname()}", int(themes[theme].getbold()))

    draw = ImageDraw.Draw(img)

    msg = name

    draw.text(get_text_align(msg, font, (1024, 1024)), msg, (int(themes[theme].getcolor1()), int(themes[theme].getcolor2()), int(themes[theme].getcolor3())), font=font)
    img.save(f"render/outputs/{name}{theme}.png")
    return f"render/outputs/{name}{theme}.png"
