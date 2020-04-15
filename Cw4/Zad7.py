class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow

    def pokaz_gdzie_jestes(self):
        print(f"Jesteś w: x={self.x}, y={self.y}")

gra = Robaczek(0, 0, 1)
gra.idz_w_gore(5)
gra.idz_w_dol(2)
gra.idz_w_lewo(20)
gra.idz_w_prawo(7)
gra.pokaz_gdzie_jestes()