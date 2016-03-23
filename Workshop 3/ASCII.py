lower = 10
upper = 100
userInput = input("Enter a number (" + str(lower) + "-" + str(upper) + "):")

for i in range(lower, upper + 1, 1):  # make sure we have integers of different 'length'
    print("{:>5} {:>5}".format(i, chr(i)))
