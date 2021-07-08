print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/TREASURE____ISLAND___/
'''
)

print("v****************** Welcome to the Treasure Island ******************")
print("Your mission is to find the treasure \n")

game_over = '''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}

GAME OVER
'''
beast = '''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
'''

lock_door = '''
                            __________
                           |  __  __  |
                           | |  ||  | |
                           | |  ||  | |
                           | |__||__| |
                           |  __  __()|
                           | |  ||  | |
                           | |  ||  | |
                           | |  ||  | |
                           | |  ||  | |
                           | |__||__| |
    Locked to death        |__________|

'''

treasure = '''
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'


'''

direction = input(
    "You are at the cross road, where you want to go? Type 'left' or 'right'? ").lower()

if direction == "left":
    action = input(
        "You come to a lake. There is an island at the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim across? "
    )
    if action == "swim":
        color = input(
            "You have arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which color do you choose? "
        )
        if color == "red":
            print("You have entered the room of beasts.Game Over")
            print(beast)
        elif color == "yellow":
            print(lock_door)
        elif color == "blue":
            print("You've got what you came for...")
            print(treasure)
    else:
        print(game_over)
elif direction == "right":
    print(game_over)
else:
    print("Type left or right")