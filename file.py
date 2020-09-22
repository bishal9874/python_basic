num = int(input("enter the number to check prime or not"))
for i in range(1,num):
    if(num % i == 0):
        print("not prime")
        break
else:
    print("prime")