def fib():
    x = 0
    y = 1
    while 1:
        yield x
        temp = x
        x = y
        y = temp + x

ciag = fib()
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())
print(ciag.__next__())