import random
MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
price = INITIAL_PRICE
day = 0
print("Starting price ${:,.2f}".format(price))
while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    priceChange = 0
# generate a random integer of 1 or 2
# if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    print("current day {1} ${0:,.2f} ".format(price, day))
