matrix =[
    [3,4,5],
    [5,7,8],
    [4,9,7]
]
print(matrix)
transposed=[]
#for colem
for i in range(3):
    list=[]
    for row in matrix:
         list.append(row[i])
    transposed.append(list)
print(transposed) 

#same 
trans =[[row[i] for row in matrix] for i in range(3)]
print(trans)