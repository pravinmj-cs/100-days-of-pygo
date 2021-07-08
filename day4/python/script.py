# Tried with some other solution that using normal if-else conditionals

from random import randint


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

data_dict = [
    {"type": rock, "name": "Rock", "value": 0, "winning_value": 1,
        "winning_type": paper},
    {
        "type": paper,
        "name": "Paper",
        "value": 1,
        "winning_value": 2,
        "winning_type": scissor
    },
    {
        "type": scissor,
        "name": "Scissor",
        "value": 2,
        "winning_value": 0,
        "winning_type": paper
    },
]

computer_choice = randint(0, 2)

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

try:
    print(f"\n You chose {data_dict[choice]['name']}")
    print(data_dict[choice]["type"])

    print(f"The compter choose {data_dict[computer_choice]['name']}")
    print(data_dict[computer_choice]["type"])

    if computer_choice == choice:
        print("\n Its a Draw")
    elif data_dict[choice]["winning_value"] == computer_choice:
        print("Computer Won")
    else:
        print("You Won")
except IndexError:
    print("Choose a value of 0,1,or 2")
