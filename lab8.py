# 33. Write a program to calculate the monthly income of a person using the following commission schedule:


monthly_sales_income = int(input("enter monthly sales income:"))

if monthly_sales_income >= 50000:
    print(f"montly income of a person in rupees:", 375 + ((monthly_sales_income / 100) * 16))
    
elif monthly_sales_income <= 50000 and monthly_sales_income >= 40000:
    print(f"montly income of a person in rupees:", 350 + ((monthly_sales_income / 100) * 14))
    
elif monthly_sales_income <= 40000 and monthly_sales_income >= 30000:
    print(f"montly income of a person in rupees:", 325 + ((monthly_sales_income / 100) * 12))
    
elif monthly_sales_income <= 30000 and monthly_sales_income >= 20000:
    print(f"montly income of a person in rupees:", 300 + ((monthly_sales_income / 100) * 9))
    
elif monthly_sales_income <= 20000 and monthly_sales_income >= 10000:
     print(f"montly income of a person in rupees:", 250 + ((monthly_sales_income / 100) * 5))
    
elif monthly_sales_income <= 10000:
     print(f"montly income of a person in rupees:", 200 + ((monthly_sales_income / 100) * 3))


# 34. Write a program to read a 3-digit number and find whether the middle digit is numerically equal to the sum of the other two digits and prints an appropriate response.

n = str(input("enter number:"))

if int(n[1]) == int(n[0]) + int(n[2]):
    print(f"{n[1]} is numerically equal to the sum of {n[0]} and {n[2]}")
    
else:
    print(f"{n[1]} is numerically not equal to the sum of {n[0]} and {n[2]}")
    

# 35. A Company insures its drivers in the following cases.
#1. If the driver is married.
#2. If the driver is unmarried, male and above 30 years of age.
#3. if the driver is unmarried, female and above 25 years of age.
#In all other cases, the driver is not insured. If the marital status, sex, age of the driver are the inputs, write a program to determine whether the driver is insured or not.

marital_status = str(input("enter marital status:"))
gender = str(input("enter gender:"))
age = int(input("enter drivers age:"))

if marital_status == "Yes":
    print("driver is insured")
    
elif marital_status == "No" and gender == "Male" and age >= 30:
    print("driver is insured")
    
elif marital_status == "No" and gender == "Female" and age >= 25:
    print("driver is insured")
        
else:
    print("driver is not insured")