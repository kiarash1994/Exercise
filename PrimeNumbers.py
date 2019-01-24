def PrimeNums(x):
    #x = input()
    j = 0
    for i in range(1,x):
        if x%i == 0:
            j+=1
    if j == 1:
        return x
    else:
        return 0
num = input("Enter your number please:")
for s in range (2,num):
    x = PrimeNums(s)
    if x > 0:
        print(x)