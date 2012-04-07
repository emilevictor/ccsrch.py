import random

class CreditCardNumber:
    def __init__(self, length):

        """Issuer should have 6 digits"""
        self.issuer = str(random.randrange(100000,999999))
        self.verifiedCardNumber = ""

       # if (len(self.issuer) < 6):
        #    self.issuer += "0"*(6-len(self.issuer))

        #print (self.issuer)
       
        lowRange = int('1' + '0' * (length-8))
        highRange = int('9' * (length-7))
        self.accountNumber = str(random.randrange(lowRange,highRange))
        #if (len(self.accountNumber) < 9):
        #    self.accountNumber += "0"*(9-len(self.accountNumber))

        #print (self.accountNumber)

        for i in range(0,9):
            if self.luhn(self.issuer + self.accountNumber + str(i)) == True:
                self.verifiedCardNumber = self.issuer + self.accountNumber + str(i)

        """Now calculate luhn number for the account number"""

    def luhn(self, cardNumber):
        """Luhn Formula implementation sourced from http://en.wikipedia.org/wiki/Luhn_algorithm"""
        num = [int(x) for x in str(cardNumber)]
        return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0        

    def toString(self):
        """Print the number to a string"""
        if (self.verifiedCardNumber != ""):
            print(self.verifiedCardNumber[0])
            print(self.verifiedCardNumber)

    def toFormattedString(self):
        output = ""
        for i in range(0,len(self.verifiedCardNumber)):
            output += self.verifiedCardNumber[i]
            if (i+1) % 4 == 0:
                #print(i)
                output += " "
        if(output != ""):
            print(output)
