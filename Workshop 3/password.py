MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTER = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
valid = False
password = input("Please enter a valid password\nYour password must be between 5 and 15 characters, and contain:\n1 or more uppercase characters\n1 or more lowercase characters\n1 or more numbers\nand 1 or more special characters: !@#$%^&*()_-=+`~,./o'[]\<>?O{}|")
password_length = len(password)
while not valid:
    valid = False
    symbol = False
    upper_case = False
    for char in password:
        if char in SPECIAL_CHARACTER:
            symbol = True
        if char.isupper():
            upper_case = True

    if symbol and upper_case:
        print("valid")




# print("Password is Invalid")
# password = input("Please enter a valid password\nYour password must be between 5 and 15 characters, and contain:\n1 or more uppercase characters\n1 or more lowercase characters\n1 or more numbers\nand 1 or more special characters: !@#$%^&*()_-=+`~,./o'[]\<>?O{}|")
# print("Your {} character password {} is Valid!".format(password_length, password))
# symbols = "!@#$"
# password = input("?: ")
# valid = False
# for char in symbols:
#     if char in password:
#         valid = True
# print(valid)
