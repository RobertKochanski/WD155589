A = [1/x for x in range(1,11)]

B = [2**x for x in range(0,11)]

C = [x for x in B if x % 4 == 0]

print(f"{A}")
print(f"{B}")
print(f"{C}")