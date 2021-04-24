d={1:100,2:200,3:300}
print(d ,"d")
d2=d.copy()
print(d2,"d2") 
s={}.fromkeys(['adarsh','prashant','rahule'],0)
print(s)
print(d.keys())
print(d.values())
k={}
print(dir())
#diasnory comprihention
h={'a':1,'b':2}
for pair in d.items():
    print(pair)
new={k:v for k,v in h.items() if v>1}
print(new)
n={k + c:v * 2 for k,v in h.items() if v>0}
print(n)