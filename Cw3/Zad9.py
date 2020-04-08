def ciag(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        x = 1
        for i in liczby:
            x *= i
        return x

print(ciag())
print(ciag(1, 2, 3, 4, 5))