#find num is prime using while loop
num = int(input("ENTER NUMBER:  "))

while num >= 1:
    if num % 1 == 0 and num % num == 0:
        print(num,"Number is prime ")
        break
    else:
        print( num, "is not prime number")
        break

