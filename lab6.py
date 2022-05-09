# 27. Write a program to find biggest of given three numbers.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a > b:
    print("biggest number is {a}")

elif b > c:
    print("biggest number is {b}")

else:
    print("biggest number is {c}")

# 28. Write a program to check whether the given year is leap year or not.

days = int(input("enter number of days in a year:"))

if days <= 365:
    print("given year is normal year")
    
else:
    print("given year is leap year")

# 29. Write a program to find the roots of a given quadratic equation and print the nature of roots.

# quadratic equation = ax ** 2 + bx + c = 0

a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))

d = ((b ** 2) - (4 * a * c))

if d == 0:
    root1 = root2 = -b / (2 * a)
    print("roots are real and equal:", (root1, root2))
    
elif d > 0:
    root1 = (-b + (d) ** 0.5) / (2 * a)
    root2 = (-b - (d) ** 0.5) / (2 * a)
    print("roots are reaal and unequal:", (root1, root2))
    
elif d < 0:
    root1 = (-b + (d) ** 0.5) / (2 * a)
    root2 = (-b - (d) ** 0.5) / (2 * a)
    print("roots are imaginary:", (root1, root2))