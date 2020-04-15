class ciag_a:
    a1 = 0
    r = 0
    n = 0

    def wyswietl_dane(self):
        print(f"a1 = {self.a1}\nr = {self.r}\nn = {self.n}")

    def pobierz_elementy(self):
        print(f"a1 = {self.a1} a2 = {self.a1+self.r} a3 = {self.a1+2*self.r}")

    def pobierz_parametry(self):
        self.a1 = int(input("a1 = "))
        self.r = int(input("r = "))
        self.n = int(input("n = "))

    def policz_sume(self):
        return ((2 * self.a1) + (self.n - 1) * self.r) / 2 * self.n

    def policz_elementy(self):
        return self.a1 + (self.n - 1) * self.r

ciag = ciag_a()
ciag.pobierz_parametry()
ciag.wyswietl_dane()
ciag.pobierz_elementy()
print(ciag.policz_sume())
print(ciag.policz_elementy())