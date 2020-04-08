def foo(a):
    if a>0:
        print("Funkcja rosnąca")
    elif a==0:
        print("Funkcja stała")
    else:
        print("Funkcja malejąca")

print(foo(1))
print(foo(0))
print(foo(-1))