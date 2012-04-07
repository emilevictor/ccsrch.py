# Script by Emile Victor
# https://github.com/emilevictor
# Takes as input a credit card number (no spaces) and outputs whether
# it passes the Luhn formula.

def is_luhn_valid(cc):
    num = [int(x) for x in str(cc)]
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

print("Hi! This script was written by Emile Victor for the COMS3000\n\
course at UQ St Lucia.\n\
Please input a credit card number WITHOUT spaces or other characters.\n\
It must have 16 characters.\
      ")
ccNum = input('Insert the credit card number here: ')
if is_luhn_valid(ccNum) == True:
    print("THIS IS A VALID CREDIT CARD NUMBER")
else:
    print("NOPE. NOT VALID.")

