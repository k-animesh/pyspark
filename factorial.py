#calculate factorial of given number using for loop
num = int(input("ENTER NUMBER"))
fac = 1
for i in range(1,num+1):
    fac*=i
print(fac)