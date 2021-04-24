s1={1,2,3,4,5,6}
s2={2,4,6}
#union operation 
print(s1|s2)
print(s1.union(s2))
#intersection 
print(s1&s2)
print(s1.intersection(s2))
#semetric difference 
print(s1^s2)
print(s1.symmetric_difference(s2))
#difference
print(s1-s2)
#subset 
print(s1.issubset(s2))
print(s2.issubset(s1))
