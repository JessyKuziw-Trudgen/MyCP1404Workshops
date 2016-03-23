# A shipping company requires a small program that would allow them to quickly work out total shipping charge
# for a number of items.
# The program allows the user to enter the number of items and the shipping cost per item. Then the program
# computes and displays the total shipping cost.
# If the total shipping cost is over $100, then a 10% discount is applied to the total shipping cost before the
# amount is displayed on the screen.

numberOfItems = float(input("Enter the number of items:"))
shippingCostPerItem = float(input("Enter shipping cost per item:"))

totalShippingCost = numberOfItems * shippingCostPerItem
if totalShippingCost > 100:
    totalShippingCost -= totalShippingCost * 0.10
print("Total shipping cost is: $", '{0:.2f}'.format(totalShippingCost), sep="")
