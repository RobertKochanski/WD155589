class NaZakupy:
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(f"{self.nazwa_produktu} {self.ilosc} {self.jednostka_miary} {self.cena_jed}")

    def ile_produktu(self):
        print(f"{self.ilosc} {self.jednostka_miary}")

    def ile_kosztuje(self):
        return (self.ilosc * self.cena_jed)

zakupy = NaZakupy("czekolada", 2, "szt.", 2.49)
zakupy.wyswietl_produkt()
zakupy.ile_produktu()
print(zakupy.ile_kosztuje())
