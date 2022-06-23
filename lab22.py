#Write a program to print the following triangle.
#1
#1 1
#1 2 1
#1 2 3 1
#1 2 3 4 1

n = int(input())

for i in range(0, n):
    for j in range(1, i + 1):
        print(j, end = " ")
        
    print(1)
