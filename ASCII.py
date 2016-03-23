def main():

    lower = 10
    upper = 100

    for i in range(lower, upper + 1, 1):  # make sure we have integers of different 'length'
        print("{:>5} {:>5}".format(i, chr(i)))


def get_number(lower, upper):
    user_input = input("Enter a number ({} - {}):".format(lower, upper))
    number_valid = False
    while not number_valid:
        if not user_input.isdecimal():
            user_input = input("Enter a number ({} - {}):".format(lower, upper))
        elif upper < lower:
            user_input = input("Enter a number ({} - {}):".format(lower, upper))
        else:
            number_valid = True
    return user_input
