# Exercise 2 Shopping Cart Program

item = input("What item do you wanna buy? ")
price = float(input("What is the price ($)? "))
quantity = int(input("How many items do you wanna buy? "))

total = price * quantity

print(f'You bought {quantity} unit(s) of {item}!')
print(f'It cost ${total:.2f}.')
