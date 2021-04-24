num =int(input(" 2 ko chor k likhna sodh chal rha 2 pe "))
for i in range(2,num):
    while (num % i)==0:
        print(num ,"no is not prime :")
        print(i,"times",num//i ,"is ",num)
        break
    else:
        print(num ,"no is prime")
        break