# . “Quick Pick” Lottery Ticket Generator
# Write a program that asks the user how many “quick picks” they wish to generate. The program then
# generates that many lines of output. Each line consists of six random numbers between 1 and 45.
# Each line should not contain any repeated number. Each line of numbers should be displayed in
# ascending order.
# Your code should produce output that matches the sample output (except the numbers are random):
# How many quick picks? 5
# 9 10 11 32 38 44
# 2 9 12 14 28 30
# 5 10 16 22 35 42
# 1 2 16 22 37 40
# 1 17 20 23 25 27
from random import randint

HIGH = 45
NUMBERS_IN_LIST = 6

quick_pick_range = int(input("Enter number of quick picks: "))
for i in range(0, quick_pick_range):
    quick_picks = []
    for picks in range(0, NUMBERS_IN_LIST):
        number = randint(1, HIGH)
        while number in quick_picks:
            number = randint(1, HIGH)
        quick_picks.append(number)
    for number in sorted(quick_picks):
        print("{:2}".format(number), end=' ')
    print('')
