mat =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat)
trans=[]
for i  in range(3):
    x=[]
    for row in mat:
        x.append(row[i])
    trans.append(x)
print(trans)
    