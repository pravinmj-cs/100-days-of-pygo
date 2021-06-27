# better way is declare a passowrd list, shuffle and apped to list. instead of concat to string(costly in terms of performance as new string is created everytime)

from random import choice, shuffle

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("Welcome to the password generator")
try:
    nr_letters = int(
        input("How many letters would you like in you password? \n"))
    nr_symbols = int(input("How many symbols would you like? \n"))
    nr_numbers = int(input("How many numbers would you like? \n"))
    generated_pwd = ""
    for l in range(nr_letters):
        generated_pwd += choice(letters)

    for s in range(nr_symbols):
        generated_pwd += choice(symbols)

    for n in range(nr_numbers):
        generated_pwd += choice(numbers)
    c2list = list(generated_pwd)
    generated_pwd = "".join(c2list)
    print(f"The generated passowrd is: {generated_pwd}")
except ValueError:
    print("Enter only numbers")
