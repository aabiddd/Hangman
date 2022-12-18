import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) #letters in the word
    alphabets = set(string.ascii_uppercase)
    used_letters = set() #user's guess

    difficulty = ''
    while 1:
        print('Easy(e), Medium(m) and Hard(h)')
        difficulty = input('Enter Difficulty:')
        if (difficulty == 'e') or (difficulty == 'm') or (difficulty == 'h'):
            break

    if difficulty == 'e':
        lives = 10
    elif difficulty == 'm':
        lives = 8
    else:
        lives = 6

    while len(word_letters) > 0 and lives > 0:
        #data shown
        print('Remaining Lives: ', lives, 'and the letters you have used:', ' '.join(used_letters))
        # print(used_letters, word, word_letters)
        #current guessed word
        currently_guessed = [letter if letter in used_letters else '-' for letter in word]
        print('Status:', ' '.join(currently_guessed))
        
        #user's input:
        input_letter = input('Enter a letter: ').upper()
        if input_letter in alphabets - used_letters:
            used_letters.add(input_letter)
            if input_letter in word_letters:
                word_letters.remove(input_letter)
            else:
                lives = lives - 1

        elif input_letter in used_letters:
            print('You have already used this letter. Try another one!')
        
        else: 
            print('Invalid Letter!!!')

    if lives == 0: 
        print(f"You Lost. The Correct Word was {word}")
    else:
        print(f'CONGRATULATIONS!! You guessed the word {word} correctly.')
hangman()