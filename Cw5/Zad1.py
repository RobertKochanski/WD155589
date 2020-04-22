class material:
    rodzaj = ""
    dlugosc = 0
    szerokosc = 0

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(f"{self.rodzaj}")

class ubrania(material):
    rozmiar = ""
    kolor = ""
    dla_kogo = ""

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(f"{self.rodzaj}, {self.dlugosc}, {self.szerokosc}, {self.rozmiar}, {self.kolor}, {self.dla_kogo}")

class sweter(ubrania):
    rodzaj_swetra = ""

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        super().__init__(rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print(f"{self.rodzaj}, {self.dlugosc}, {self.szerokosc}, {self.rozmiar}, {self.kolor}, {self.dla_kogo}, {self.rodzaj_swetra}")


m = material("bawełna", 65, 36)
u = ubrania("jedwab", 88, 55, "L", "czarny", "Siebie")
s = sweter("poliester", 66, 44, "M", "czerwony", "Kolega", "z golfem")

m.wyswietl_nazwe()
u.wyswietl_dane()
s.wyswietl_dane()