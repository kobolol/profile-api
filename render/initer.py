from render.utils.theme import Theme
from render.utils.readfile import readfile
from render.utils.render_worker import render_worker
import os


def render_pic(themes, name, theme):
    if theme == "None" or name == "None" or len(themes)-1 < int(theme):
        return "error"

    if not os.path.exists(f"render/outputs/{name}{theme}.png"):
        print("Anfrage noch nicht gerendert, Wird nun erstellt ...")
        filename = render_worker(name, int(theme), themes)
        return filename

    else:
        print("Anfrage wurde schon gerendert, wird nun übergeben ...")
        return f"render/outputs/{name}{theme}.png"


def load_themes():
    file = open("render/themelist.txt", "r")
    liste = readfile(file)
    file.close()
    return liste
