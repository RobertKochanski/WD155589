def foo(a1,a2):
    if a1==a2:
        print("Proste są równoległe")
    elif a1*a2==-1:
        print("Proste są prostopadłe")
    else:
        print("Proste nie są ani równoległe ani prostopadłe")

print(foo(4,4))
print(foo(4,(-1/4)))
print(foo(6,8))