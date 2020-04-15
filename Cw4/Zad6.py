class Slowa:
    wyraz1 = ""
    wyraz2 = ""

    def __init__(self, wyraz1, wyraz2):
        self.wyraz1 = wyraz1
        self.wyraz2 = wyraz2

    def sprawdz_czy_palindrom(self):
        if(self.wyraz1 == self.wyraz1[::-1]):
            print("wyraz1 jest palindromem")
        else:
            print("wyraz1 nie jest palindromem")

    def sprawdz_czy_metagramy(self):
        roznice = 0
        if(len(self.wyraz1) == len(self.wyraz2)):
            for i in range(len(self.wyraz1)):
                if(self.wyraz1[i] != self.wyraz2[i]):
                    roznice += 1
            if(roznice == 1):
                print("wyrazy są metagramami")
        print("wyrazy nie są metagramami")

    def sprawdz_czy_anagramy(self):
        temp = 0
        if(len(self.wyraz1) != len(self.wyraz2)):
            return False
        lista1 = list(self.wyraz1)
        lista1.sort()
        lista2 = list(self.wyraz2)
        lista2.sort()
        if(lista1 == lista2):
            print("wyrazy są anagramami")
        else:
            print("wyrazy nie są anagramami")

    def wyswietl_wyrazy(self):
        print(f"wyraz1 = {self.wyraz1}, wyraz2 = {self.wyraz2}")

slowa = Slowa("kajak", "kajak")
slowa.wyswietl_wyrazy()
slowa.sprawdz_czy_palindrom()
slowa.sprawdz_czy_metagramy()
slowa.sprawdz_czy_anagramy()


