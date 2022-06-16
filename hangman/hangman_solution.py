'''
make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        print("init")
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
        
       
        word = random.choice(word_list)
        self.word_guessed = "_" * len(word)
        
        
        print("The mystery word has", {len(word)}, "characters")
        print(self.word_guessed)
        

    def check_letter(self,letter,word,num_lives,list_letters,guessed_flag):
        print("check")
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        # TODO 3: Check if the v is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        
        
        if letter not in word:
            print("check2")
            
            num_lives -= 1
            print("Sorry, ",letter," is not in the word.")
            print("You have ",{num_lives}," lives left.")

            list_letters.append(letter)
            print("check3")
            return self.ask_letter(word_list)

        else:
            print("ask2")
            self.word_guessed.replace("_",letter)
            print("Nice",(letter)," is in the word")
            print("_", "where word_guessed now has unveiled the ,",(letter))
            print("check4")
            list_letters.append(letter)
            print("check5")
            word_as_list = list(self.word_guessed)
            indices = [i for i, letterr in enumerate(word) if letterr == letter]
            print("check6")
            for index in indices:
                word_as_list[index] = letter
            self.word_guessed = "".join(word_as_list)
            guessed_flag = False
            if "_" not in self.word_guessed:
                guessed_flag = True
                return self.dennis()

    def dennis(guessed_flag,word):
        if guessed_flag is True:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


            
    def ask_letter(self,word_list):
        print("ask")
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method

        
        list_letters = []

        word = random.choice(word_list)
        

        word = random.choice(word_list)

        guessed_flag = False

        num_lives = 5

        while not guessed_flag and num_lives > 0:
            letter = input("Please guess a letter: ")
            if len(letter) == 1 and letter.isalpha():
                if letter in list_letters:
                    print("{letter} was already tried")
                else:
                    self.check_letter(letter,word,num_lives,list_letters,guessed_flag)
            else:
                print("Please, enter just one character")
                print("Not a valid guess.")
            
            print(self.word_guessed)
            print("\n")

        
def play_game(word_list):
    print("play")
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)



    print(game)
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word

    return game.ask_letter(word_list)
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon','sunildennis']
    
    
    play_game(word_list)
