def hangman():
    print('H A N G M A N')

    secret_word = 'python'

    player_word = input('Guess the word: ')

    if player_word == secret_word:
        return print('You survived!')
    else:
        return print('You lost!')


hangman()
