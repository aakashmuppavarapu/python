# 17. Rajesh’s basic salary is input through the keyboard. His D.A. is 40% of basic salary, and H.R.A. is 20% of basic salary. Write a program to calculate his gross salary.

basic_salary = int(input("enter base salary:"))
DA = (basic_salary * 40) / 100
HRA = (basic_salary * 20) / 100
gross_salary = basic_salary + DA + HRA

print(f"D.A:", DA)
print(f"H.R.A:", HRA)
print(f"gross salary:", gross_salary)

# 18. The distance between two cities in Km. is input through the keyboard. Write a program to convert and print the result in meters and centimeteres.


distance_between_two_cities = int(input("enter distance in km:"))

meters = distance_between_two_cities / 0.001
centimeters = distance_between_two_cities / 0.0000100

print(f"meters:", meters)
print(f"centimeters:", round(centimeters, 2))

# 19. Write a program which accepts the amount in dollars and convert into rupees.

amount_in_dollars = int(input("enter amount in dollars:"))

inr = 76.72 * amount_in_dollars

print(f"amount in rupee:", inr)

# 20. Write a program to read your address and print it.

address = str("flat : 203; mig : 532, 533; road no : 1; kphb colony; hyderabad; telangana; 500072.")

print(f"address:", address)

# 21. Write a program to print the area of a triangle if b and h values are given.

b = int(input("enter base:"))
h = int(input("enter height:"))

area_of_triangle = 1 / 2 * (b * h)

print(f"area of triangle:", area_of_triangle)

# 22. Write a program to print the area of a triangle if three sides are given.

a = int(input("enter_first_side:"))
b = int(input("enter_second_side:"))
c = int(input("enter_third_side:"))

perimeter = s = (a + b + c) / 2
area_of_triangle = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"perimeter:", s)
print(f"area_of_triangle:", round(area_of_triangle, 2))