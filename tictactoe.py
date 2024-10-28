import random

def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            printBoard(xState, zState)
            print("X Won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            printBoard(xState, zState)
            print("O Won the match")
            return 0
    return -1

def play_game():
    xState = [0] * 9
    zState = [0] * 9
    print("Welcome to Tic Tac Toe")
    opponent = input("Do you want to play against another player or computer? (player/computer): ")
    if opponent.lower() == "player":
        turn = 1  # 1 for X and 0 for O
    elif opponent.lower() == "computer":
        turn = random.choice([0, 1])
        print("You are playing against the computer.")
    else:
        print("Invalid choice. Please try again.")
        return

    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            if opponent.lower() == "player":
                print("O's Chance")
                value = int(input("Please enter a value: "))
                zState[value] = 1
            elif opponent.lower() == "computer":
                available_moves = [i for i in range(9) if xState[i] == 0 and zState[i] == 0]
                computer_choice = random.choice(available_moves)
                print(f"Computer chooses {computer_choice}")
                zState[computer_choice] = 1
            else:
                print("Invalid choice. Please try again.")
                return

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            play_again = input("Do you want to play again? (yes or no): ")
            if play_again.lower() == "yes":
                play_game()
            else:
                break
        turn = 1 - turn

if __name__ == "__main__":
    play_game()
