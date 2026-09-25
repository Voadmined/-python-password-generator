# Version 1.0.0
# PyLock Password Generator [Special Edition]

import random as ran
import questionary as quest

upCharacters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

lowCharacters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
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
passLength = int(
    quest.text(
        "Desired password length:",
        validate=lambda answer: answer.isdigit()
    ).ask()
)

print()
selected = quest.checkbox(
    "Choose the character types:",
    choices=[
        "Upper Case Letters",
        "Lower Case Letters",
        "Numbers",
        "Symbols"
    ]
).ask()
print()

possibleCharacters = []

if "Upper Case Letters" in selected:
    possibleCharacters.extend(upCharacters)

if "Lower Case Letters" in selected:
    possibleCharacters.extend(lowCharacters)

if "Numbers" in selected:
    possibleCharacters.extend(numbers)

if "Symbols" in selected:
    possibleCharacters.extend(symbols)

passwordArray = []

for _ in range(passLength):
    slctChar = ran.randint(0, len(possibleCharacters)-1)
    passwordArray.append(possibleCharacters[slctChar])

password = "".join(passwordArray)
print("Password: ", password)
print()