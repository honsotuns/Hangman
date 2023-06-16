# Hangman game

A PYTHON PROGRAM THAT ALLOWS A PLAYER TO GUESS THE ALPHABETS OF FRUITS

 1: Setting up the environment, Setting  up  GitHub repository.


 2: Creating variables for the game

  * Creating a list containing the names of my 5 favorite fruits. Assigning this list to a variable called word_list.
  * Printing out the newly created list to the standard output.

  * Choose a random word from the list using random.choice method
  * Asking the player for an input 
  * Codes to request input from the player, using input() function

  * Check that the input is a single character using "if" statement
  * Creating an "if" statement that checks "if" the length of the input is equal to 1 and the input is an alphabet
  * In the body of the "if" statement, print a message that says "Good guess!" If the player guessed the right alphabet
  

3: Check if the guessed character is in the word

  * Iteratively check if the guessed character is in the word_list
  * Creating functions to run the checks
  * Converting the word guess to lower case
  * Creating an "else" block that prints "Oops! That is not a valid input." if the preceeding conditions are not met /  If the player enters alphabet that is not in the guess word
  
  

4: Creating the game class
  
  * Creating a class Hangman
  * Inside the class, created an init method to initialise the attributes of the class. Passed in word_list and num_lives as parameters. Making num_lives a default parameter and set the value to 5.
  * Initialised the following : 
     * word: The word to be guessed, picked randomly from the word_list

     * word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. 
      If the player guesses    'a', the list would be ['a', '', '', '', ''].

     * num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

     * num_lives: int - The number of lives the player has at the start of the game.

     * word_list: list - A list of words.

     * list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.
  * Created methods for running the checks
  * Created an "if" statement that checks if the guess is in the word
  * If word guess is not in the word:
    * In the check_guess method, Created an "else" statement:

      * Within the else block:

      * Reduced `num_lives' by 1.

      * print a message saying "Oops, {letter} is not in the word."

      * print another message saying "You have {num_lives} lives left."
  * Called the ask_for_input method to test code.

5: Code the logic of the game
  * Created a function called play_game that takes word_list as a parameter
    * Create a variable called num_lives and assign it to 5

    *  Created an instance of the Hangman class

    * Passed  num_lives as argument to the game object
    * Called the play_game function


