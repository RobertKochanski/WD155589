def foo(**lista):
    ilosc = 0
    for i in lista:
        ilosc = ilosc + lista[i]
    return ilosc

print(foo(bułka=4, kiełbasa=2, pomidor=5))
