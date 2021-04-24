list=['one' , 'two' , 'three' , 'four']
if 'two' in list :
    print('hai be two')
if 'six' not in list:
    print('nhi hai be ')

list.reverse()
print(list)

no = [2,8,1,5,9,4]
sorted_list=sorted(no)
print("sorted_list: ",sorted_list)
print("orignal list : ", no)
print("reverse shorted list : ",sorted(no,reverse=True))
no.sort()
print(no)