from ccNum_class import CreditCardNumber
import sys


length = 16
if len(sys.argv) == 1:
    numberOfCCNumbers = input('How many fake credit cards do you want generated: ')
    numberOfCCNumbers = int(numberOfCCNumbers)
    length = input("How long should they be: ")
elif len(sys.argv) == 2:
    numberOfCCNumbers = int(sys.argv[1])
elif len(sys.argv) == 3:
    numberOfCCNumbers = int(sys.argv[1])
    length = int(sys.argv[2])

for i in xrange(0, numberOfCCNumbers):
    x = CreditCardNumber(length)
    x.toFormattedString()
