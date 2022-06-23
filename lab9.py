# 36. Write a program to read the characters continuously until ‘$’ is given and display the number of characters enter.

n = 0

while True:
    
    if n == '$':
        break
        
    else:
        n = input()

# 37. Write a program to read a character and find out whether it is uppercase or lowercase.

n = input("enter a character")

if (n.isupper()):
    print("Char is Uppercase")
    
else:
    print("char is Lowercase")

# 38. Write a program to print the uppercase letter of a given lowercase.

n = input("Enter character")

a = n.upper()
print(a)

# 38. Write a program to print the uppercase letter of a given lowercase.
#second method

n = input("Enter character")

a = n.swapcase()
print(a)

# 39. Write a program to check whether the given input is digit or lowercase character or uppercase character or a special character.

n = input("Enter character")

if (n.isdigit()):
    print("Given char is digit")
    
elif (n.isupper()):
    print("Given char is Upper case")

elif (n.islower()):
    print("Given char is Lower case")
    
else:
    print("Given char is Special character")

# 40. Write a program to check whether the given alphabet is a vowel or consonant.

n = input("Enter alphabet")

if n in ('a', 'e', 'i', 'o', 'u'):
    print("Given alphabet is Vowel")
    
else:
    print("Given Alphabet is Consonant")