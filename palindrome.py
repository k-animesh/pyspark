my_str= ["maharastra", "rotator"]

for i in my_str:
    if my_str[::-1]== my_str:
        print(i + " is a palindrome")
    else:
        print(i +" is not a palindrome")