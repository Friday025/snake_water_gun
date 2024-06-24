import random

logo = """

 ____              _           ____                        
/ ___| _ __   __ _| | _____   / ___|_   _ _ __             
\___ \| '_ \ / _` | |/ / _ \ | |  _| | | | '_ \            
 ___) | | | | (_| |   <  __/ | |_| | |_| | | | |           
|____/|_| |_|\__,_|_|\_\___|  \____|\__,_|_| |_|           
__        __    _               ____                       
\ \      / /_ _| |_ ___ _ __   / ___| __ _ _ __ ___   ___  
 \ \ /\ / / _` | __/ _ \ '__| | |  _ / _` | '_ ` _ \ / _ \ 
  \ V  V / (_| | ||  __/ |    | |_| | (_| | | | | | |  __/ 
   \_/\_/ \__,_|\__\___|_|     \____|\__,_|_| |_| |_|\___| 
     

"""

gun = """

     +--^----------,--------,-----,--------^-,
    | |||||||||   `--------'     |          O
    `+---------------------------^----------|
    `\_,---------,---------,--------------'
        / XXXXXX /'|       /'
        / XXXXXX /  `\    /'
    / XXXXXX /`-------'
    / XXXXXX /
    / XXXXXX /
    (________(                
    `------'              

"""

water = """"

               _            
              | |           
__      ____ _| |_ ___ _ __ 
\ \ /\ / / _` | __/ _ \ '__|
 \ V  V / (_| | ||  __/ |   
  \_/\_/ \__,_|\__\___|_|   
                            

"""

snake = """
             ____
            / . .\
            \  ---<
             \  /
   __________/ /
-=:___________/

"""


print(logo)


game_image = [snake, water, gun]

player_score = 0

computer_score = 0

game_input = {-1: snake, 0: water, 1: gun}

game_over = True

while game_over:

    user_input = int(input("Enter what you want to choose (-1 for snake, 0 for water, 1 for gun) : "))
    print(f"user choice is {game_input[user_input]}")
    print(game_input[user_input])
   

    computer_input = random.randint(-1, 1)
    print(f"computer choice is {game_input[computer_input]}")
    print(game_input[computer_input])
    

# game logic
    if user_input >1 :
        print("your input is not vaild please choose between 0 to 2 ....")

    else:

        if user_input == computer_input:
            print("Its Draw!")

        elif user_input == -1 and computer_input == 0: 
            print("You Win!")
            player_score +=1
        elif user_input ==-1 and computer_input == 1:
            print("You Lose!")
            computer_score +=1
        elif user_input == 0 and computer_input == 1: 
            print("You Win!")
            player_score +=1
        elif user_input == 0 and computer_input == -1:
            print("You lose!")
            computer_score +=1
        elif user_input == 1 and computer_input == -1: 
            print("You Win!")
            player_score +=1
        elif user_input == 1 and computer_input == 0:
            print("You lose!")
            computer_score +=1

        is_play = input("Do you want to play again type (y / n )  : ").lower()
        if is_play == "n":
            game_over = False
            print(f"user_score is {player_score}, \ncomputer_score is {computer_score}")
            break
