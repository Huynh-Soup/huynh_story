"""
Write a program that will take a number (Integers only) and
return a statement that will let the user know if it is even or odd
"""
number = float(input("Say a number and I will determine if it is even or odd: "))

if (number%2 == 0):
    print( str(number) + " is even ")
    
elif (number%2 == 1):
    print( str(number) + " is odd ")
    
else:
    print("Boi, this aint it chief ")