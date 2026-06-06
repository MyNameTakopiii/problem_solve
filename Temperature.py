def to_fahrenheit(celsius: float):
    result = ((9 * celsius) + 32)
    return f'{result} Fahrenheit'

def to_kelvin(celsius: float):
    result = ((5 * celsius) + 273)
    return f'{result} Kelvin'

def to_reaumur(celsius: float):
    result = (4 * celsius)
    return f'{result} Reaumur'

in_celsius = (float(input()) / 5)
to_unit = str(input())
if to_unit == "F":
    print(to_fahrenheit(in_celsius))
elif to_unit == "K":
    print(to_kelvin(in_celsius))
elif to_unit == "R":
    print(to_reaumur(in_celsius))