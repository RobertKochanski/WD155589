slownik = {
    "bułka": "sztuki",
    "mleko": "sztuki",
    "cukierki": "kg",
    "ser": "kg"
}

lista = [i for i in slownik if slownik[i] == "sztuki"]

print(lista)