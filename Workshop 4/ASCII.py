LOWER = 10
UPPER = 100


def get_number(lower, upper):
    if lower > upper:
        return lower

    user_input = input("Enter a number ({} - {}):".format(lower, upper))
    number_valid = False
    while not number_valid:
        if user_input.isdecimal() and lower <= int(user_input) <= upper:
            number_valid = True
        else:

            user_input = input("Enter a number ({} - {}):".format(lower, upper))
    return user_input

print(get_number(LOWER, UPPER))
print(get_number(UPPER, LOWER))
