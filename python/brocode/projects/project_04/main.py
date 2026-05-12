# Temperature converter program

temperature = float(input("Enter the value of the temperature you want to convert: "))
unit = input("Is the temperature in Celsius or Fahrenheit (Enter C or F): ")

if unit == "C" or unit == "c":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f'The temperature equals to {fahrenheit:.1f}°F')
elif unit == "F" or unit == "f":
    celsius = (temperature - 32) * 5 / 9
    print(f'The temperature equals to {celsius:.1f}°C')
else:
    print("Please enter a valid option.")
