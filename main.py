from flask import *
from render.initer import load_themes, render_pic
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
dirs = os.path.join(THIS_FOLDER, "render/outputs")
for f in os.listdir(dirs):
        os.remove(os.path.join(dirs, f))

themes = load_themes(THIS_FOLDER)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def create_pic():
    name_query = str(request.args.get("name"))
    theme_query = str(request.args.get("t"))

    filename = render_pic(themes, name_query, theme_query, THIS_FOLDER)

    if filename == "error":
        return "<h1>error</h1><br><h3>check if theme exist or name & theme is given!</h3>"

    return send_file(filename, mimetype='image/gif')


if __name__ == "__main__":
    app.run()
