import random


def hangman():
    print("H A N G M A N")

    words = ("python", "java", "swift", "javascript")

    secret_word = random.choice(words)

    new_word = secret_word[0:3]

    for _ in range(3, len(secret_word)):
        new_word += "-"

    player_word = input(f"Guess the word {new_word}: ")

    if player_word == secret_word:
        return print("You survived!")
    else:
        return print("You lost!")


hangman()
