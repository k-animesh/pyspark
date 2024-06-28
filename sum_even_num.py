#find sum of all even numbers from 1 to 20 using while loop


sum = 0
i=1
while i<=20:
    if i % 2==0:
        sum += i
    i+=1
print(sum)


