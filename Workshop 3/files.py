nameFile = open("name.txt", 'w')
name = input("Enter your name:")
print(name, file=nameFile)
nameFile.close()

nameFile = open("name.txt", 'r')
name = nameFile.read().strip()
print("Your name is: {}".format(name))
nameFile.close()

numberFile = open("numbers.txt", "r")
number1 = int(numberFile.readline())
number2 = int(numberFile.readline())
print(number1 + number2)
numberFile.close()
