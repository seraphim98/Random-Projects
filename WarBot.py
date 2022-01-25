"""
A code that simulates random battles between "players" until only one remains
Author: James Horlock
Version 25/01/22
"""

import random
import os.path
import os
def user_input():

    """
    Function takes a series of user inputs to be used as players
    :return: player_list: all the inputs stored as strings in a list
    """
    continue_process = True
    player_list = []
    print("Once you are finished adding players enter: EXIT")
    while continue_process == True:

        if len(player_list) % 2 != 0:
            print("Odd number of players will result in certain players being considered more than once")
        new_player = input("Please enter the name of the next player: ")
        if new_player == "EXIT":
            continue_process = False
        else:
            player_list.append(new_player)

    return player_list


def fight(player_1, player_2):

    """
    Decides fight by assigning integers to each player, winner is player with the large number
    :param player_1: name of player 1 as string
    :param player_2: name of player 2 as string
    :return: outcome as boolean
    """

    choice_1 = random.randint(0, 10)
    choice_2 = random.randint(0, 10)
    print(player_1 + " VS " + player_2)
    if choice_1 > choice_2:
        print(player_1 + " WINS!")
        outcome = True
    else:
        print(player_2 + " WINS!")
        outcome = False

    return outcome

def file_read(f):
    """
    Reads given file and returns content
    :param f: name of text file as string
    :return:  contents of file as list
    """
    open_file = open(f, 'r')
    players = open_file.read().splitlines()
    return players


def main():

    # Allows user to choose input type and only accept valid ones
    invalid_input = True
    while invalid_input:
        input_choice = input("Do you wish to input players from file: (Y/N) ")
        if input_choice == "Y" or input_choice == "y":
            print("Ensure players are separated by new lines in text file")
            #makes sure that given file is of right format, exists and has data
            exist_check = True
            while exist_check:
                file = input("Please give the name of the text file to be read: ")
                if os.path.isfile(file) and ".txt" in file and os.stat(file).st_size != 0:
                    exist_check = False
                    current_players = file_read(file)
                    invalid_input = False
                else:
                    print("Chosen file does not exist, is not a .txt file or is empty")
                    print("Please enter a valid file name")

                    exit_clause = input("If you wish to use a different input method enter exit,"
                                    " to continue enter anything:")
                    if exit_clause == "exit":
                        break

        # allows for user input
        elif input_choice == "N" or input_choice == "n":
            current_players = user_input()
            invalid_input = False

        else:
            print("INVALID INPUT")

        if invalid_input:
            end_code = input("If you wish to end code please enter exit, to continue enter anything:")

            if end_code == "exit":
                exit()

    latest_players = []
    num_of_players = len(current_players)
    # game loop continues until only one player remains

    while num_of_players > 1:
        if num_of_players % 2 == 0:
            for i in range(num_of_players):
                if i % 2 == 0:
                    if fight(current_players[i], current_players[i+1]):
                        latest_players.append(current_players[i])
                    else:
                        latest_players.append(current_players[i+1])
        else:
            for i in range(num_of_players):
                if i != num_of_players - 1:
                    if i % 2 == 0:
                        if fight(current_players[i], current_players[i + 1]):
                            latest_players.append(current_players[i])
                        else:
                            latest_players.append(current_players[i + 1])
                else:
                    if fight(latest_players[0], current_players[i]):
                        pass
                    else:
                        # player 1 loses they are removed from the list and replaced with player 2
                        del latest_players[0]
                        latest_players.append(current_players[i])

        #updates list to contain all players that one this round
        current_players = latest_players
        latest_players = []
        num_of_players = len(current_players)
    print("The winner of this war is : " + current_players[0])

main()


