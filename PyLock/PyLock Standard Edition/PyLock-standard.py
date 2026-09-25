# Version 1.0.2
# PyLock Password Generator [Standard edition]

import random as ran

characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",

    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

symbols = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".",
    "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`",
    "{", "|", "}", "~"
]

print()
passLength = int(input("Desired password length: "))

passwordArray = []

for _ in range(passLength):

    varType = ran.randint(1, 3)

    if varType == 1:
        slctChar = ran.randint(0, len(characters)-1)
        passwordArray.append(characters[slctChar])
    
    elif varType == 2:
        slctNum = ran.randint(0, len(numbers)-1)
        passwordArray.append(numbers[slctNum])

    elif varType == 3:
        slctSym = ran.randint(0, len(symbols)-1)
        passwordArray.append(symbols[slctSym])

password = "".join(passwordArray)

print()
print("Password:", password)
print()

passwordArray = []