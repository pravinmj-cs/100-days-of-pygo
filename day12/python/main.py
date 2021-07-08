
""" 
    A number guessing program that has three levels of difficulty: easy, medium, hard.
    
"""

from random import randint


print("Welcome to the Number Guessing game")
print("I'm thinking of a number between 1 and 100")

difficulty = ""
i = 0
while difficulty.lower() != 'easy' and difficulty.lower() != "hard":
    if i == 0:
        print("You can choose difficulty between 'easy' and 'hard'\n")
    elif i > 0 and (difficulty.lower()) != 'easy' and (difficulty.lower()) != 'hard':
        print("Enter either 'easy' or 'hard'.")
    i = i+1
    difficulty = input("Choose a difficulty: ")
    print(difficulty)


def make_guess(actual_no, guessed_no):
    """ Guess if actual no is above or below guessed_no
    Args:
        actual_no(int):     actual no set by program
        guessed_no(int):    number required to be checked against the actual_no 
    Returns:
        (str): validated message
    """
    if actual_no > guessed_no:
        msg = "Too Low"
    elif actual_no < guessed_no:
        msg = "Too High"
    elif guessed_no not in range(1, 100):
        msg = "Number not in range of 1 to 100"
    elif actual_no == guessed_no:
        msg = "Correct"
    return msg


levels = {
    "easy": 15,
    "medium": 10,
    "hard": 5
}

set_no = randint(1, 100)
set_counter = levels[difficulty]


while set_counter > 0:
    guessed_num = int(input("Guess a Number between 1 and 100: "))
    response = make_guess(set_no, guessed_num)
    if response == "Correct":
        print(f"You got it. The answer is {set_no}")
        exit()
    else:
        set_counter -= 1
        print(response, "\n")

print("Game over")
