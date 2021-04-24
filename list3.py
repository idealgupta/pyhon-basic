list=[1,1,1,2,2,3,3,3,4,4,5,5,5,5]
b ="one,two,three"
abc=list
abc.append(6)
print(list)
blist=b.split(',')
print(blist)
print(list[1])
print(list[-1])
print(list[0])
print(list[0:4])
print(list[::2])
print(list.count(4))
c =['one','two']
new_list=list + c
print(new_list)
for ele in c:
    print(ele)

square = []
for i in range(10):
    square.append(i**2)
print(square)

square=[i**2 for i in range(10)]
print(square)
list_1=[2*i for i in list]
print(list_1)
c=[(i,2*i) for i in range(10)]
print(c)