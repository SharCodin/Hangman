# Title: Hangman
# Author: Sharvin
# Description:
#       Select a random word and hide the letters.
#       Player will guess a letter belonging to word.
#       If correct, letter will be revealed.
#       If wrong, lose 1 life.
#       Game continues until player reveals all letters or all lives are lost.
# Date Modified: 01:50 14/06/2020
# Version: 1.0

# importing modules
import random
from words_data import words

player_lives = 5

board = [" " for x in range(0, 20)]
word_list = []
word_length = 0
player_word_length = 0
word = "placeholder"

def print_board():
    initial_board_empty = f" {board[0]} {board[1]} {board[2]} {board[3]} {board [4]} {board[5]} {board[6]} {board[7]} {board[8]} {board[9]} {board[10]} {board[11]} {board[12]} {board[13]} {board[14]} {board[15]} {board[16]} {board[17]} {board[18]} {board[19]}"
    print(initial_board_empty)

def initial_board(word):
    """Count the number of alphabet in word and multiply the string "_ " by it to make a starting board"""
    for m in range(len(word)):
        global word_length
        board[m] = "_"
        word_length += 1

def askForInput():
    print(f"Remaining lives: {player_lives}")
    print()
    print_board()
    print()
    player_input_new = input("enter an alphabet and press enter: ")
    check(player_input_new)
    return

def check(player_input_new):
    """"Check if the alphabet entered by player is in word. """
    answer = player_input_new.strip().lower()
    try:
        if int(answer) in range(0, 10):
            print("Only one alphabet is allowed: ")
            askForInput()
    except:
        if len(answer) == 1:
            check_answer(answer)
        else:
            print("Only one alphabet is allowed: ")
            askForInput()
    return

def check_answer(answer):
    if answer in word_list:
        global player_word_length
        a = 0
        for x in word_list:
            if answer == x:
                board[a] = x
                player_word_length += 1
            a += 1
        check_win_lose()
    else:
        global player_lives
        player_lives -= 1
        print(f"You lose a life. \nRemaining lives: {player_lives}")
        check_win_lose()
    askForInput()

def check_win_lose():
    global player_lives
    global word
    if player_lives <= 0:
        print("You lose! ")
        print(f"The correct word is: {word}")
        next_game = input("Next game? (Y/N): ").strip().lower()
        if next_game == "y":
            new_game()
        else:
            quit()
    else:
        if player_word_length == word_length:
            print("You win!")
            next_game = input("Next game? (Y/N): ").strip().lower()
            if next_game == "y":
                new_game()
            else:
                quit()
    return 

def new_game():
    global word_list
    global word_length
    global player_word_length
    global board
    global player_lives
    global word
    word_list = []
    board = [" " for x in range(0, 20)]
    word_length = 0
    player_word_length = 0
    player_lives = 5
    word = random.choice(words)
    word_list = [x for x in word]
    initial_board(word)
    askForInput()

# starting the game
new_game()