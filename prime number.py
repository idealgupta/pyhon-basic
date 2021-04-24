num =int(input("no likh be "))
if num > 1 :
    for i in range(2,num):
        while (num %i == 0):
            print("prime nhin hai be ")
        else:
            print("prime hai be :{}".format(num))
print("tu to pahle hi chud gya be ")