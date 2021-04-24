a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
"""
if (a>b) and (a>c) :
    print("a is greter : ",a)
elif (b>c) and (b>c) :
    print("b is greter : ",b)
else :
    print("c is greter : ",c)
"""
if (a>b) and (a>c) :
    larger = a
elif (b>c) and (b>c) :
    larger = b
else :
    larger = c
print("the larger no is :",larger)