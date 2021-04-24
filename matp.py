mat=[
    [2,4,5],
    [2,4,5],
    [2,4,5]
]
print(mat)
transposed=[]
for i in range(3):
    list=[]
    for row in mat:
        list.append(row[i])
    transposed.append(list)
print(transposed)

tra=[[row[i] for row in mat] for i in range(3)]
print(tra)