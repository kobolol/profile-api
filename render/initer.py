from render.utils.theme import Theme
from render.utils.readfile import readfile
from render.utils.render_worker import render_worker
import os


def render_pic(themes, name, theme, THIS_FOLDER):
    file = os.path.join(THIS_FOLDER, f"render/outputs/{name}{theme}.png")

    if theme == "None" or name == "None" or len(themes)-1 < int(theme):
        return "error"

    if not os.path.exists(file):
        print("Anfrage noch nicht gerendert, Wird nun erstellt ...")
        filename = render_worker(name, int(theme), themes, THIS_FOLDER)
        return filename

    else:
        print("Anfrage wurde schon gerendert, wird nun übergeben ...")
        return file


def load_themes(THIS_FOLDER):
    file = open(os.path.join(THIS_FOLDER, "render/themelist.txt"))
    liste = readfile(file)
    file.close()
    return liste
