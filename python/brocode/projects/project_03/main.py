# Weight converter program
# This program converts weights in kilogram to pounds and vice-versa

weight = float(input("Enter your weight: "))
option = input("Choose the weight type you want to convert: 1 (kilogram to pounds) - 2 (pounds to kilogram): ")

if option == '1':
    pound = weight * 2.205
    print(f"You weight in pounds is {pound:.2f}lbs.")
elif option == '2':
    kilogram = weight / 2.205
    print(f"You weight in kilogram is {kilogram:.2f}kgs.")
else:
    print("Please, enter a valid option.")
