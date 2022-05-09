# 11.Write a program to convert speed of a vehicle given in km/hour to miles/hour.

kmph = float(input("enter speed of vehicles in kmph:"))

mph = (kmph) / 1.609344

print(f"miles/hour:", round(mph, 2))

# 12.Write a program to convert the given seconds into hours – minutes – seconds.

seconds = int(input("enter number of seconds:"))

hours = seconds / 3600
minutes = seconds * 0.0166666667
seconds = seconds * 1

print(f"hours:", round(hours, 5))
print(f"minutes:", round(minutes, 5))
print(f"hours-minutes-seconds:", round(hours, 5), round(minutes, 5), seconds)

# 13.A milk vendor buys milk at the rate of 3.25/lt then adds a litre of water for every 4 litres of milk and sells the water milk at the rate of 4.15 per lt. Calculate the gain for milk vendor.


cost_price = float(input("enter cost price:",))
selling_price = float(input("enter selling price:"))
number_of_liters_with_water = 5

total_cost_price = cost_price * (number_of_liters_with_water)
total_selling_price = selling_price * (number_of_liters_with_water)
total_profit_gained = total_selling_price - total_cost_price
profit_gained_perliter = total_profit_gained / 5


print(f"total cost price:", total_cost_price)
print(f"total selling price:", total_selling_price)
print(f"total profit gained:", total_profit_gained)
print(f"profit gained per liter:", profit_gained_perliter)

# 14.The temperature of the city is input through the keyboard in Fahrenheit. Write a program to convert into Celsius.

fahrenheit = int(input("enter temparature in fahrenheit:"))

celsius = (fahrenheit - 32) / 1.8000

print(f"temperature in celsius:", round(celsius, 3))

# 15.Two numbers are input into two locations ‘a’ and ‘b’. Write a program to interchange the contents of ‘a’ and ‘b’ without using temporary variables.

a = int(input("enter value of a:"))
b = int(input("enter value of b:"))

(a, b) = (b, a)

print("interchang:", (a, b ))

# 16. Given the coordinates of two points (x1, y1) and (x2, y2). Write a program to find the distance between these two points.

x1 = int(input("enter x1:"))
y1 = int(input("enter y1:"))
x2 = int(input("enter x2:"))
y2 = int(input("enter y2:"))

distance_between_two_points =  ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"distance between (x1, y1) and (x2, y2):", round(distance_between_two_points, 3))