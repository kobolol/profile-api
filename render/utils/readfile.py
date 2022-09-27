from render.utils.theme import Theme


def readfile(file):
    liste = []
    i = 0
    nummer = ""
    dataname = ""
    bold = ""
    fontname = ""
    color1 = ""
    color2 = ""
    color3 = ""
    for line in file:
        if i == 0:
            nummer = line.rstrip()
            i += 1
        elif i == 1:
            dataname = line.rstrip()
            i += 1
        elif i == 2:
            bold = line.rstrip()
            i += 1
        elif i == 3:
            fontname = line.rstrip()
            i += 1
        elif i == 4:
            color1 = line.rstrip()
            i += 1
        elif i == 5:
            color2 = line.rstrip()
            i += 1
        elif i == 6:
            color3 = line.rstrip()
            i += 1
        elif i == 7:
            i = 0
            print("Geladendes Thema: ", nummer, dataname, bold, fontname, color1, color2, color3)
            liste += [Theme(nummer, dataname, bold, fontname, color1, color2, color3)]

    return liste
