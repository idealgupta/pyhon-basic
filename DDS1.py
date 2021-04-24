#empty disnory 
my_dist={}
print(type(my_dist))
#integer key disnory
dis2={1:'adarsh',2:'rahul',3:'arshad'}
print(dis2)
#empty dis using dict
d =dict()
print(d)
#dis with mix keys 
a ={'name':'chintu',1:['abc','xyz']}
print(a)
#create using with list of  tupple 
b=dict([(1,'abs'),(2,'bhb')])
print(b)
details={'gf name':'nibbi ','bf name':'nibba','age':20,'whatsaap no':889900776655}
print(details['gf name'])
details['age']=25
print(details)
details['gf whatsaap ']=12345678
print(details)
#remove items
details.pop('age')
print(details)
del dis2[1]
print(dis2)
dis2.clear()
print(dis2)