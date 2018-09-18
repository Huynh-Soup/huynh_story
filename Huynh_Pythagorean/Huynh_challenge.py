print("Hello, this is the challenge where you input values for a b and c so I can determine what type of triangle it is")
a = int(input("What is your value of a: "))
b = int(input("What is your value of b: "))
c = int(input("What is your value of c: "))


"""
If statements
"""


if (c**2 > a**2 + b**2):
    print("That triangle is Obtuse")
if (c**2 < a**2 + b**2):
    print("That triangle is acute")
if (c**2 == a**2 + b**2):
    print("That triangle is a right triangle")
    
else:
    print("That is not a triangle")