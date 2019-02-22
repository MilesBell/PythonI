#1. gets personal information from the user
#2. 
print("User information")
name=input("Hi. What is your name?")
age=int(input("How old are you?"))
weight=float(input("Finally, how much do you weigh? In lbs."))
print("Hello",name,"you're", age, "and you weigh", weight, "lbs")
#3.
print("\nYour name in uppercase is:")
print(name.upper())

print("\n& in lowercase it's:")
print(name.lower())
#4.
print("\nYour name ten times is:")
calling=input(name*10)
print(calling)
#5.
print("You have been alive for", age*365*24*60*60, "seconds!")
#6.
print("\nOn the moon, you would weigh", weight*0.156, "lbs")
print("\nWhile on the sun, you would be about", weight*1.07, "lbs")
#7. 
input("\nExit using the 'enter' key")




