class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


proba1 = "Ala ma kota"
wspak = Wspak(proba1)
for x in proba1:
    print(wspak.__next__())

print("////////")

proba2 = [3, 5, 9, 6, 2]
wspak = Wspak(proba2)
for x in proba2:
    print(wspak.__next__())