class Theme:
    def __init__(self, nummer, dataname, bold, fontname, color1, color2, color3):
        self.__Nummer = nummer
        self.__Dataname = dataname
        self.__Bold = bold
        self.__Fontname = fontname
        self.__Color1 = color1
        self.__Color2 = color2
        self.__Color3 = color3

    def getnummer(self):
        return self.__Nummer

    def getdataname(self):
        return self.__Dataname

    def getbold(self):
        return self.__Bold

    def getfontname(self):
        return self.__Fontname

    def getcolor1(self):
        return self.__Color1

    def getcolor2(self):
        return self.__Color2

    def getcolor3(self):
        return self.__Color3
