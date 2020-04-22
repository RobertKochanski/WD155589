def samogloski(data):
    samogl = ('a', 'A', 'ą', 'Ą', 'e', 'E', 'ę', 'Ę', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y')
    for znak in data:
        for x in samogl:
            if znak == x:
                yield znak


napis = samogloski("Generator")
print(napis.__next__())
print(napis.__next__())
print(napis.__next__())
print(napis.__next__())


