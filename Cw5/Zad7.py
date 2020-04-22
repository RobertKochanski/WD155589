class IndeksParzysty:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.data) - 1:
            raise StopIteration
        self.index += 2
        return self.data[self.index]


tablica = [5, 6, 7, 8, 9, 3, 5, 7, 8]
proba = IndeksParzysty(tablica)
print(proba.__next__())
print(proba.__next__())
print(proba.__next__())
print(proba.__next__())
print(proba.__next__())
