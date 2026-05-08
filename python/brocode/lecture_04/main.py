# input() = function prompts the user to enter data and returns a string 

name = input("What is your name? ")
age = int(input("What is your age? "))

age = age + 1
# age = int(age) + 1

print(f'Hello {name}.')
print('Tomorrow is your birthday!')
print(f'You are {age} years old.')
