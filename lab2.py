#Write a program to find the area and circumference of a circle.
#Write a program to find the area of a sphere.
#Write a program to find the volume of a cylinder

r1 = int(input("radius of circle:"))
r2 = int(input("radius of sphere:"))
r3 = int(input("radius of cylinder:"))
h = int(input("height of cylinder:"))
pi = (round(22/7, 2))

a = pi * (r1 ** 2)
b = 2 * pi * r1
c = 4 * pi * (r2 ** 2)
d = pi * (r3 ** 2) * h

print(f"area of circle:", a)
print(f"circumference of circle:", round(b, 2))
print(f"area of sphere:", c)
print(f"volume of cylinder:", round(d, 2))

#Write a program to find your age in days

age = int(input("enter the age:"))
days_in_a_year = int(input("number of days in a year:"))

age_in_days = age * days_in_a_year

print(f"age in days:", age_in_days)

#Write a program to find the simple interest.

principal = int(input("enter principal:"))
tenure = int(input("enter tenure:"))
interest_rate = float(input("enter interest rate:"))

simple_interest = principal * tenure * interest_rate/100

if principal > 10000:
    simple_interest = simple_interest + 2000

if tenure > 12:
    simple_interest = simple_interest + 1000
    
if interest_rate > 1:
    simple_interest = simple_interest + 500

print(f"simple interest:", (simple_interest))

#Write a program to find the compound interest.

principal = int(input("enter principal:"))
interest_rate = float(input("enter interest rate:"))
nt = int(input("enter number of years:"))
n = int(input("enter number of times interest is compounded per year:"))

amount = principal * (1 + (interest_rate/n)) ** nt
compound_interest = amount - principal

print(f"amount:", amount)
print(f"compound interest:", compound_interest)