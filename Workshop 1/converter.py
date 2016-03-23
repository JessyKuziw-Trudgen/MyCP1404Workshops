def main():
    print('Temperature Conversion program')

    celsiusValue = float(input('Enter celsius value:'))
    fahrenheitValue = celsius_fahrenheit_converter(celsiusValue)
    kelvinValue = celsiusValue + 273.13

    print('Celsius value:', celsiusValue)
    print('Fahrenheit value:', fahrenheitValue)
    print('Kelvin Value:', kelvinValue)


def celsius_fahrenheit_converter(celsiusValue):
    fahrenheitValue = celsiusValue * 9 / 5 + 32
    return fahrenheitValue
