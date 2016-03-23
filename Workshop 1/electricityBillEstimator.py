TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

pricePerKWh = float(input('Enter the Tariff number, 11 or 31:'))

if pricePerKWh == 11:
    pricePerKWh = TARIFF_11
else:
    pricePerKWh = TARIFF_31

dailyUse = float(input('Enter daily electricity use in kWh:'))
billingDays = float(input('Enter number of billing days:'))

billEstimate = pricePerKWh * dailyUse * billingDays

print('Your estimated bill is: $', "{0:.2f}".format(billEstimate), sep='')
