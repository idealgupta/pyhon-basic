a=int(input("starting : "))
b=int(input("last : "))
for num in range (a,b):
    if (num%2)!=0:
        print(num)
        continue