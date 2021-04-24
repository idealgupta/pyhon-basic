list=[2,3,4,5,6,7,8]
list_1=[2**i for i in list]
print(list_1)
print(list_1[:2:3])
list_1.reverse()
print(list_1)
print(len(list_1))
a=list_1.pop(2)
b=list.pop(2)
print("valu of a : ",a)
print("value of b is : ",b)
c=a+b
print("adding a and b : ",c)
list_1.append(c)
print(list_1)
print(list_1.sort())
print(sorted(list_1))
print(sorted(list_1,reverse=True))
for i in list_1:
    if (i>60):
        break
    print(i)
new_list=i.split('')
print(new_list)