def calc_bmi(weight, height):
    bmi = weight / height**2
    return bmi


def main():
    weight = float(input('Enter your weight in kilograms:'))
    height = float(input('Enter your height in meters:'))

    bmi = calc_bmi(weight, height)

    print('Your bmi is:', bmi)
