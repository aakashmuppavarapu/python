# 30. Write a program to read positive numbers continuously until negative number is given by using ‘if’.

n = 0

while True:
    
    if n < 0:
        break
    else:
        n = int(input())

# 31. Write a program to read ten numbers and print their sum by using ‘if’ statement.

sum = 0       

for i in range(1, 11):
    
    if i > 0:
        i = int(input())
        sum += i

print("sum of given number:", sum)

# 32. Write a program to read three sides a, b, c of a triangle and print the type of the triangle

a = int(input("enter side a:"))
b = int(input("enter side b:"))
c = int(input("enter side c:"))


if a + b >= c and b + c >= a and c + a >= b:
    print("triangle is valid")
    
    if a == b == c == a:
        print("type of triangle:", "equilateral trangle")
    
    elif a == b or b == c or c == a:
        print("type of triangle:", "isosceles triangle")
    
    elif a != b or b != c or c != a:
        print("type of triangle:", "scalene trinagle")
    
else:
    print("triangle is invalid")