
import random


'''  A class of a Hangman game, where player guess fruits words '''
class Hangman:
    
    ''' init method with word_list and num_lives as parameters '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters =  len(set(self.word))
        self.list_letters = []
        print(f'The mistery word has {len(self.word)} characters')
        print(self.word_guessed)
        
    ''' The check letter method which checks all conditions for an input to be accepted '''
    def check_letter(self, letter):
        if letter in self.word.lower():
            if self.word.count(letter) > 1:
                idx = 0
                for _ in range(self.word.count(letter)):
                    idx = self.word.index(letter, idx)
                    self.word_guessed[idx] = letter
                    idx += 1
            idx = self.word.lower().index(letter)
            self.word_guessed[idx] = letter
            self.num_letters -= 1
            print(f'Good guess! {letter} is in the word!')
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Oops, {letter} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

        self.list_letters.append(letter)
        
    ''' The ask letter method which takes an input from the player '''   
    def ask_letter(self):
        while True:
            letter = input('Enter a character: ').lower()

            if letter in self.list_letters:
                print(f"{letter} was already tried")
            elif len(letter) > 1:
                print('Please, enter just one character')
            else:
                break

        self.check_letter(letter)
        
''' The play game method which initialises the game '''
def play_game(word_list):
    game = Hangman(word_list)
    
    while True:
        game.ask_letter()
        if game.num_lives == 0:
            print(f'Sorry you ran out of lives. The word was {game.word}')
            break
        elif game.num_letters == 0:
            print('Wow congratulations, you won!')
            break
    

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
