my_str = "I am an aspiring data engineer"
vowels=['a','e','i','o','u']
count = 0
for i in my_str:
    if i in vowels:
        count+=1
print(count)
