# if = do some code only if some condition is True
# else, do something else

age = int(input("What is your age? "))

if age >= 100: # The order is important!!!!!!!!!! If age >= 18 would be first the code would never come to the age >=100 condition
    print("You are too old to have a credit card!") # I would never say that!
elif age >= 18:
    print("You can have a credit card!")
elif age <= 0:
    print("Invalid age!")
else:
    print("You can not have a credit card yet.")



response = input("\nWould you like some food? (yes/no): ")

if response == "yes":
    print("Great! Have some food!")
elif response == "no":
    print("Ok, no food for you!")
else:
    print("Invalid option.")



# input verification using if statement
name = input("\nWhat is your name? ")

if name == "":
    print("You didn't type your name!")
else:
    print(f"Hello, {name}!")



# an if statement do not need condition verification with boolean values
online = True

if online:
    print("\nYou are connected!")
else:
    print("You are offline!")
