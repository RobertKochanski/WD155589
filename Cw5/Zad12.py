miesiace = (miesiac for miesiac in ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
                                    "Lipiec", "Sierpień", "Październik", "Listopad", "Grudzień"])

for x in range(11):
    print(miesiace.__next__())
