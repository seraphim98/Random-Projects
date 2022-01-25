"""""
A simple game of hangman code that outputs to the terminal. 
Author: James Horlock
Version: 25/01/22
"""""


import random
import enchant

def word_selection():
    """""
    Module that random selects a word if there is no user input from a small list of words.
    
    :return: word as  string
    """""
    words = ["Queen", "Pizza", "Penguin", "Clinic", "Seven", "Floccinaucinihilipilification", "Peanut", "Walrus",
             "Blooming", "Guitar", "Hippopotamus", "Television", "Smelly", "Dog", "Floor", "Plants", "Mjolnir", "Pog"]
    word = random.choice(words)

    return word


def build_structure(counter, build_array):
    """
    This function updates the build array to account for incorrect guesses.

    :param counter: current number of incorrect guesses as integer
    :param build_array: current state of built structure as array
    :return: build_array: updated build state after incorrect guess as array
    :return: current_build: current state of build for printing to terminal as list
    """
    current_build = []

    if counter == 1:

        current_build.append(build_array[0][0])

    elif counter == 2:

        for j in range(len(build_array[0]) - 1):

            index = len(build_array[0]) - j - 2
            current_build.append(build_array[0][index])

    elif counter > 2:
        if build_array[0][counter - 2] != build_array[1][counter - 2]:

            build_array[0][counter - 2] = build_array[1][counter - 2]

        for j in range(len(build_array[0])): current_build.append(build_array[0][j])


    return build_array, current_build

def letter_find(word, guess, revealed_letters):

    """
    This function find the location of guessed letters withing the given word.

    :param word: word that is being determined as string
    :param guess: guessed letter as string
    :param revealed_letters: current known leters of word as string
    :return: update_revealed: latest revealed letter after guess as string
    :return: remaining_letters: number of unknown letters as integer
    """

    indices = [i for i, x in enumerate(word) if x == guess]
    count = len(indices)
    update_revealed = str()

    for i in range(len(word)):

        if i in indices:

            update_revealed += guess

        elif revealed_letters[i] != "-":

            update_revealed += revealed_letters[i]

        else:
            update_revealed += "-"

    return update_revealed, count

def main():

    #asks if user wants to choose their own word
    dictionary = enchant.Dict("en_GB")
    invalid_input = True
    while invalid_input == True:
        start_input = input("Do you want to use your own word : (Y/N) ")
        if start_input == "Y" or start_input == "N" or start_input == "y" or start_input == "n":
            invalid_input = False
        else:
            print("INVALID INPUT")

    invalid_input = True
    #if user chooses to give a word this ensures that it is an english word
    if start_input == "Y" or start_input == "y":
        while invalid_input == True:
            selected_word = input("Please enter your word: ")
            if dictionary.check(selected_word) == True:
                invalid_input = False
            else:
                print("Input not an english word please try again")
    #if no input is desired a random word form a selected list is given
    else:
        selected_word = word_selection()
    #creates a blank line indicating the number of letters in a word
    revealed_letters = str()
    for i in range(len(selected_word)):
        revealed_letters += "_"
    #clears the terminal so a second player will not see the given word
    for i in range(50):
        print("\n")
    print("Your word is : " + revealed_letters)
    incorrect_guess = 0
    #creates an array containg all possible variations of the build
    build_array = (["____", "   |", "   |", "   |", "   |", "____"],
                   ["____", " | |", " O |", "-|-|", " ^ |", "____"])
    invalid_guess = True
    previous_guesses = []
    remaining_letters = len(selected_word)
    #game loop that ensures that the game ends after 6 incorrect guesses
    while incorrect_guess < 6:

        while invalid_guess == True:

            guess = input("Please enter your guess: ")
            if guess == "PLEASEEND":
                exit()
            if guess.isalpha() == False or len(guess) > 1:
                print("Invalid input: please only use one letter for your guess")
            elif guess in previous_guesses:
                print("Invalid input: you have already guessed this letter")
            else:
                invalid_guess = False
        invalid_guess = True
        #cheks if guess is in string
        if guess.lower() in selected_word or guess.upper() in selected_word:

            print(guess.upper() + " is in the word!")

            if guess.lower() in selected_word:
                revealed_letters, count = letter_find(selected_word, guess.lower(), revealed_letters)
                remaining_letters -= count
            if guess.upper() in selected_word:
                revealed_letters, count = letter_find(selected_word, guess.upper(), revealed_letters)
                remaining_letters -= count
            #ends game loop if word is guessed correctly
            if remaining_letters == 0:
                break

        else:
            print(guess + " is not in the word!")
            incorrect_guess += 1
            build_array, current_state = build_structure(incorrect_guess, build_array)

        previous_guesses.append(guess)
        print("So far your word is : " + revealed_letters)
        print("You have " + str(6 - incorrect_guess) + " lives remaining")
        #shows the current build state at that stage of the game
        if incorrect_guess != 0:
            print("Your current build state is : ")
            for i in current_state:
                print(i)


    #tells player outcome of game
    if incorrect_guess == 6:
        print("GAME OVER: YOU ARE OUT OF LIVES BETTER LUCK NEXT TIME")
        print("Your word was : " + selected_word)
    else:
        print("Congratulations you win! Your word was : " + selected_word)

main()