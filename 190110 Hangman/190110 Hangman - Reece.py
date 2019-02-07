"""Game of hangman.
Picks a random work for the dictonary.
The user has a number of goes to guess the word, one letter at a time.
"""

import random


FILENAME = "dictionary.txt"
MAX_ALLOWED_GUESSES = 6


def get_dictionary(filename):
    
    with open(filename, "r") as file:
        all_words = file.readlines()

        return all_words


def get_random_word(all_words):

    max_lines = len(all_words)
    random_word = all_words[random.randint(0, max_lines - 1)].strip()
    
    return random_word


def get_user_guess():
    while True:
        letter = input("Please input a letter: ")
        
        if len(letter) == 1 and letter.isalpha():
            return letter.lower()
        elif len(letter) > 1 or not letter.isalpha():
            print("That is not a letter...")
            print()
        else:
            print("You have not entered a letter...")
            print()


def convert_word_to_array(random_word):
    list_of_letters = []
    
    for letter in random_word:
        list_of_letters.append(letter)
        
    return list_of_letters


def create_guessing_line(word_as_list):
    guessing_line = []
    for i in word_as_list:
        guessing_line.append("_")
    #print("START:", guessing_line)
    return guessing_line

        
def is_guess_in_word(word_as_list, guess):
    return guess in word_as_list


def print_is_guess_in_word(correct_guess, guess):
    if correct_guess:
        print("'{}' is in the word!!!".format(guess))
    else:
        print("'{}' is not in the word...".format(guess))


def any_blanks(guessing_line):
    return "_" in guessing_line


def create_word_str(guessing_line):
    word_str = ""

    for i in range(len(guessing_line)):
        word_str += guessing_line[i] + " "
    return word_str


def win_game_message(random_word):
    print()
    print("YOU WIN!!!")
    print("The word was:", random_word)

def lost_game_message(random_word):
    print()
    print("You lost...")
    print("The word was:", random_word)



def update_guessing_line(word_as_list, guess, guessing_line):
    for i in range(len(word_as_list)):
        if word_as_list[i] == guess:
            guessing_line[i] = guess
    return guessing_line


def print_max_guesses(max_guesses):
    print("You're allowed {} guesses.".format(max_guesses))

    
def print_guesses_left(max_guesses, guess_count):
    print("You have {} guesses left.".format(max_guesses - guess_count))



def main():

    game_completion_status = False
    all_words_list = get_dictionary(FILENAME)
    random_word = get_random_word(all_words_list)
    word_as_list = convert_word_to_array(random_word)
    guessing_line = create_guessing_line(word_as_list)
    

    print_max_guesses(MAX_ALLOWED_GUESSES)
    guess_count = 0
    
    while guess_count < MAX_ALLOWED_GUESSES:
        
        if not any_blanks(guessing_line):
            game_completion_status = True
            break

        print(create_word_str(guessing_line))
        print_guesses_left(MAX_ALLOWED_GUESSES, guess_count)

        
        guess = get_user_guess()
        correct_guess = is_guess_in_word(word_as_list, guess)
        print_is_guess_in_word(correct_guess, guess)

        if not correct_guess:
            guess_count += 1
            continue
        
        else:
            guessing_line = update_guessing_line(word_as_list, guess, guessing_line)
            continue


    if game_completion_status:
        win_game_message(random_word)
    else:
        lost_game_message(random_word)



if __name__ == "__main__":
    main()
        

    


