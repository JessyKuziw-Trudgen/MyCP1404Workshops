# . Write a program that prompts the user for 5 numbers and then stores each of these in a list called
# numbers. The program should then output various interesting things, as in the output below (green
# represents user input).
# Note that you can use the functions min, max, sum and len, and you can use the append method to
# add a number to a list.
# Number: 5
# Number: 20
# Number: 1
# Number: 2
# Number: 3
# The first number is 5
# The last number is 3
# The smallest number is 1
# The largest number is 20
# The average of the numbers is 6.2


numbers = []
for num in range(5):
    number = int(input('Number: '))
    numbers.append(number)
print('the first number is', numbers[0])
print('the last number is', numbers[-1])
print('the smallest number is', min(numbers))
print('the biggest number is', max(numbers))
print('the average of the numbers is', sum(numbers) / len(numbers))

