mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat)
transposed=[]
for i in range(3):
    list=[]
    for row in  mat:
        list.append(row[i])
    transposed.append(list)
print(transposed)