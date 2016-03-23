# A school teacher requires a small program that would allow primary school students to learn about various
# number sequences. The teacher is interested in a simple menu-driven console-based program that uses a
# menu for the following choices (where x and y are inputs the user enters once at the start of the program):
# 1. Show the even numbers from x to y
# 2. Show the odd numbers from x to y
# 3. Show the squares from x to y
# 4. Exit the program

x_input = int(input('Enter "x":'))
y_input = int(input('Enter "y":'))
menuChoice = int(input("Enter number for choice\n 1. Show the even numbers from x to y\n 2. Show the odd numbers from x to y\n \
3. Show the squares from x to y\n 4. Exit the program"))
remainder = x_input % 2
while menuChoice != 4:
    if menuChoice == 1:
        for number in range(x_input, y_input, 2):
            # even
            if remainder == 0:
                print(number)
            else:
                print(number +1)
    if menuChoice == 2:
        for number in range(x_input, y_input, 2):
            # odd
            if remainder == 0:
                print(number + 1)
            else:
                print(number)
    if menuChoice == 3:
        for number in range(x_input, y_input):
            print(number ** 2)
    menuChoice = int(input("Enter number for choice\n 1. Show the even numbers from x to y\n 2. Show the odd numbers from x to y\n \
3. Show the squares from x to y\n 4. Exit the program"))
