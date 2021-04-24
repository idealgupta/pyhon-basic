list_1=[1,2,3,4,5,6,7,8]
list_2=[[1,2],[3,4],[5,6]]
list_3=[1,2,3,'adarsh',4,5]
list_4=['adarsh','rahul','arshad']
print(list_1)
print(list_2)
print(list_3)
print(list_4)

#lenght
print(len(list_3))

#append add kerta hai last mai 
list_3.append('rahul')
print(list_3)

#insert list m kisi bhi jgh add krna 
list_2.insert(2,[7,8])
print(list_2)

#remove kerna list m se 
list_2.remove([3,4])
print(list_2)

#append
list_5=[2,4]
list_4.extend(list_5)
print(list_4)

#pop
a=list_1.pop(3)
print(list_1)
print(a)

