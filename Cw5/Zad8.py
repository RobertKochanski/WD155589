class samogloski:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
            self.index = -1
        else:
            print("Błąd. Zły typ danych")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.data) - 1:
            raise StopIteration
        for a in "aAąĄeEęĘiIoOuUyY":
            if self.data[self.index - 1] == a:
                self.index += 1
                return self.data[self.index]
        self.index += 1
        return self.__next__()


tekst = "Iterator"
proba = samogloski(tekst)

print(proba.__next__())
print(proba.__next__())
print(proba.__next__())
print(proba.__next__())

# a, ą, e, ę, i, o, u, y
# A, Ą, e, Ę, I, O, U, Y
