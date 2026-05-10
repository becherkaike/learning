import math

# find the hypotenuse of a right-angled triangle

# c = squared(a² + b²)

a = float(input("Enter the value of A: "))
b = float(input("Now enter the value of B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f'The hypotenuse of this right-angled triangle is {round(c, 2)}.')
