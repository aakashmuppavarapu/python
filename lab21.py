# 85. Write a program to print the Floyd’s triangle.
#1
#2 3
#4 5 6
#7 8 9 10

n = int(input())
d = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(d, end = " ")
        
        d += 1
    
    print()

# 86. Write a program to print the following triangle.
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

n = int(input())

for i in range(0, n):
    for j in range(0, i + 1):
        print(j + 1, end = " ")
        
    print()

# 87. Write a program to print the following triangle.
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5 

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end = " ")
                    
    print()