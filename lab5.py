# 23. Write a program to read the marks of 3 subjects and display the total, average, class.

maths = int(input("enter marks in maths:"))
physics = int(input("enter marks in physics:"))
chemistry = int(input("enter marks in chemistry:"))

total = maths + physics + chemistry
average = (maths + physics + chemistry) / 3

print(f"total:", total)
print(f"average:", round(average, 2))

# 24. Write a program to check whether the given number is positive or negative.

a = float(input("enter a number:"))

number = "positive or negitive"

if a > 0:
    number = "positive"
    
if a < 0:
    number = "negitive"
    
print(f"number is", number)

# 25. Write a program to find out the given number is odd or even.

a = int(input("enter a number:"))

number = "odd or even"

if a % 2 == 0:
    number = "even"
    
if a % 2 != 0:
    number = "odd"
    
print(f"number is", number)

# 26. Write a program to find smallest of given two numbers.

a = int(input("enter a:"))
b = int(input("enter b:"))

if a < b:
    print("a is small")
    
else:
    print("b is small")