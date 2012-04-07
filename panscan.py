import re

#Regexes for the different card types
mastercard = re.compile(r'(5\s*[1-5]\s*(?:\d\s*){13}\d)\D')
visa13 = re.compile(r'(4\s*(?:\d\s*){11}\d)\D')
visa16 = re.compile(r'(4\s*(?:\d\s*){14}\d)\D')
amex34 = re.compile(r'(3\s*4\s*(?:\d\s*){12}\d)\D')
amex37 = re.compile(r'(3\s*7\s*(?:\d\s*){12}\d)\D')
diners = re.compile(r'(3\s*0\s*[0-5]\s*(?:\d\s*){10}\d)\D')
jcb3 = re.compile(r'(3\s*(?:\d\s*){14}\d)\D')
jcb2 = re.compile(r'(2\s*1\s*3\s*1\s*1\s*8\s*0\s*0\s*(?:\d\s*){6}\d)\D')
regexes = [mastercard, visa13, visa16, amex34, amex37, diners, jcb3, jcb2]

def panscan(text):
    """
    Scan a string for PANs. Returns a list of pairs giving the offset and the
    actual text

    panscan(string) -> [(int, string)]
    """

    out = []
    pans = []
    for r in regexes:
        pans += r.findall(text)
    for pan in pans:
       cleanpan = pan.replace(" ", "")
       if luhn(cleanpan):
           out.append((text.index(pan), pan))
    out.sort(key=lambda p: p[0])
    return out

def luhn(cc):
    """
    Perform the luhn test on the given string. The string must contain only
    digits otherwise it will immediately return False

    luhn(string) -> bool
    """

    if not cc.isdigit(): return False
    num = [int(x) for x in str(cc)]
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

