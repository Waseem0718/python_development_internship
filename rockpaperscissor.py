#TASK 1 - ROCK PAPER SCISSOR

import random

choices = ['rock', 'paper', 'scissor']

def computer_choice():
    return random.choice(choices)

def user_choice():

    player_choice = input("Choose any one \nRock or Paper or Scissor: ").strip().lower()

    while True:
        if player_choice not in choices:
            print("Invalid choice, please try again") 
            player_choice = input("Enter Rock, Paper, or Scissor: ").strip().lower()
        return player_choice
    
def Identify_the_winner(player,computer):

    if player == computer:
        return "Its a Tie!"
    elif (player == 'rock' and computer == 'scissor') or (player == 'scissor' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        return 'You win!'
    else:
        return 'Computer wins!'     
          
    
def lets_play():

    print("lets play the game...")

    while True:
        player = user_choice()
        computer = computer_choice()
        print("user choice :",player)
        print("computer choice :",computer)
        print(Identify_the_winner(player, computer))
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break   


lets_play()