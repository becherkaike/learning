# logical operators = evaluate multiple conditions (or, and not)
#               or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

temperature = 36
is_raining = True

if temperature > 35 or temperature < 0 or is_raining:
    print("The outdoor event is canceled.\n")
else:
    print("The outdoor event is still scheduled.\n")


is_sunny = False

if temperature >= 28 and is_sunny:
    print("It is hot and sunny outside!")
elif temperature <= 10 and is_sunny:
    print("It is cold outside, but is sunny!")
elif 28 > temperature > 11 and is_sunny:
    print("It is warm and sunny outside!")
elif 28 > temperature > 11 and not is_sunny:
    print("It is warm and cloudy outside!")
elif temperature < 11 and not is_sunny:
    print("It is cold and cloudy outside!")
elif temperature > 28 and not is_sunny:
    print("It is hot and cloudy outside!")
