import random


def hangman():
    print(
        """
        H A N G M A N
        """
    )

    words = ("python", "java", "swift", "javascript")

    secret_word = random.choice(words)

    player_word = ""

    guessed_letters = ''

    for _ in range(len(secret_word)):
        player_word += "-"

    attempts = 8

    while attempts != 0:

        print(player_word)
        letter = input("Input a letter: ")

        if len(letter) > 1 or len(letter) == 0:
            print('Please, input a single letter.')
            continue

        if not letter.islower() or not letter.isalpha() :
            print('Please, enter a lowercase letter from the English alphabet.')
            continue

        if letter in player_word:
            print("You've already guessed this letter")
            continue
            
        if letter in guessed_letters and letter not in player_word:
            print("You've already guessed this letter")
            continue

        player_word = list(player_word)

        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                player_word[i] = letter

        if letter not in player_word:
            print("That letter doesn't appear in the word.")
            attempts -= 1

        player_word = "".join(player_word)
        guessed_letters += letter
        print()

        if player_word == secret_word:
            break

    print()

    if player_word == secret_word:
        print(secret_word)
        print(f"You guessed the word {secret_word}!")
        return print("You survived!")
    else:
        return print("You lost!")


hangman()
