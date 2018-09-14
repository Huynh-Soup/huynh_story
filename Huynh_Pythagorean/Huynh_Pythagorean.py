"""
Write a program that will ask the user to
enter their name and respond with a greeting using this name.
"""
name = input("Hello what is your name: ")
print("Hello " + str(name) + " Welcome to the Pythagorean simulator, we will now find")

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = float(a**2 + b**2)
print("Ok that number is now " + str(c))
