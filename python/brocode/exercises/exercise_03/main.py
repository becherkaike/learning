import math

# calculate the circunference of a circle

# C = 2 * PI * r

radius = float(input("What is the radius of the circle? "))
circumference = 2 * math.pi * radius

print(f'The circumference is {round(circumference, 2)}cm.')
