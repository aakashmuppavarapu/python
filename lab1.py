# 1.Write a program to add and subtract two numbers.
# 2.Write a program to multiply and divide two numbers.
# 3.Write a program to find the square and cube of a given number.
# 4.Write a program to find the square root of a given number.
# 5.Write a program to find the area and perimeter of a square.


a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter side of square:"))

x = a + b
y = a - b
p = a ** 2
q = b ** 3
r = a ** 0.5
g = c ** 2
h = c * 4

print(f"sum of {a} and {b} is {x}")
print(f"difference of {a} and {b} is {y}")
print(f"square of {a} is {p}")
print(f"cube of {b} is {q}")
print(f"square root of {a} is {r}")
print(f"area of square:", g)
print(f"perimeter of square:", h)