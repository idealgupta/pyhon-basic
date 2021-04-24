num =int (input("2 ki gand mero : "))
count = 0 
for i in range (2,num):
    if (num%i)==0 :
        count = count+1
        break
    if (count==1):
        print("not prime ")
    else :
        print("prmr")
