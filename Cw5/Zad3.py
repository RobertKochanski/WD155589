class Ksztalty:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, x):
        return Kwadrat(self.x + x)

    def __ge__(self, z):
        if self.x >= z.x:
            print("bok pierwszego kwadratu >= bok drugiego kwadratu")
        else:
            print("bok pierwszego kwadratu nie jest >= bok drugiego kwadratu")

    def __gt__(self, z):
        if self.x > z.x:
            print("bok pierwszego kwadratu > bok drugiego kwadratu")
        else:
            print("bok pierwszego kwadratu nie jest > bok drugiego kwadratu")

    def __le__(self, z):
        if self.x <= z.x:
            print("bok pierwszego kwadratu <= bok drugiego kwadratu")
        else:
            print("bok pierwszego kwadratu nie jest <= bok drugiego kwadratu")

    def __lt__(self, z):
        if self.x < z.x:
            print("bok pierwszego kwadratu < bok drugiego kwadratu")
        else:
            print("bok pierwszego kwadratu nie jest < bok drugiego kwadratu")


a1 = Kwadrat(4)
a2 = Kwadrat(5)

a1 > a2
a1 < a2
a1 >= a2
a1 <= a2
