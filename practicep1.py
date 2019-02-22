chapter="Introduction to PythonII"
print("original chapter name:")
print(chapter)
print("\nIn uppercase:")
print(chapter.upper())
print("\nIn 'swapcase':")
print(chapter.swapcase())
print("\nIn title format:")
print(chapter.title())
print("\nIn 'strip' format:")
print(chapter.strip())
print("\n\nPress the enter key to exit.")
print("My expenses are:")
car=input("insurance:")
gas=input("gas for my car:")
rent=input("my rent is:")
food=input("groceries and dining out:")
shopping=input("my personal shopping:")
total=car+gas+food+shopping
print("\nGrand total is:", total);
#this is good^, but adds the entered values together as a string instead of combining numeric values
#int(input( is better because it adds the integers
print("My expenses are:")
car=int(input("insurance:"))
gas=int(input("gas for my car:"))
rent=int(input("my rent is:"))
food=int(input("groceries and dining out:"))
shopping=int(input("my personal shopping:"))
total=car+gas+food+shopping
print("\nGrand total is:", total);
#below adds the entries together as a string, like 5+5+5+5 as 5555 instead of 5+5+5+5 as 20
print("My expenses are:")
car=str(input("insurance:"))
gas=str(input("gas for my car:"))
rent=str(input("my rent is:"))
food=str(input("groceries and dining out:"))
shopping=str(input("my personal shopping:"))
total=car+gas+food+shopping
print("\nGrand total is:", total);
#also adds together entries as integers, but always returns a decimal; i.e. 5+5+5+5=10.0
print("My expenses are:")
car=float(input("insurance:"))
gas=float(input("gas for my car:"))
rent=float(input("my rent is:"))
food=float(input("groceries and dining out:"))
shopping=float(input("my personal shopping:"))
total=car+gas+food+shopping
print("\nGrand total is:", total);
#practice01
#gets personal information from the user
print("\nUser\'s personal information:")
name=input("full name:")
age=input("age in years:")
weight=input("weight in lbs:")

