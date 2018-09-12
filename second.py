"""

Write a program that will ask the user what thier age is and then
determine if they are old enough to vote or not and respond appropriatlely

"""

age = int(input("Hello, how old are you?: "))

if age < 17 :
    print("You can't vote")
    
if age > 18 :
    print("Great, who would you vote for in 2020? (a,b,c) ")
    print("a. Kanye West (Yeezy) ")
    print("b.Donald Trump")
    print("c.")
