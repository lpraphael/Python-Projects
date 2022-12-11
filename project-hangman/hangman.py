import random


def hangman():
    print('H A N G M A N')

    words = ('python', 'java', 'swift', 'javascript')

    secret_word = random.choice(words)

    player_word = input('Guess the word: ')

    if player_word == secret_word:
        return print('You survived!')
    else:
        return print('You lost!')


hangman()
