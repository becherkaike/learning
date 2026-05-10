import math

# calculate the area of a circle

# A = PI * r²

radius = float(input("What is the radius of the circle? "))
area = math.pi * pow(radius, 2)

print(f'The area of the circle is {round(area, 2)}cm².')
