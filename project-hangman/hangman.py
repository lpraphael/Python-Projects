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

    for _ in range(len(secret_word)):
        player_word += "-"

    attempts = 8

    while attempts != 0:

        print(player_word)
        letter = input("Input a letter: ")

        player_word = list(player_word)

        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                player_word[i] = letter

        if letter not in player_word:
            print("That letter doesn't appear in the word.")

        player_word = "".join(player_word)
        print()
        attempts -= 1

        if player_word == secret_word:
            break

    print()
    return print("Thanks for playing!")

    # if player_word == secret_word:
    #     return print("You survived!")
    # else:
    #     return print("You lost!")


hangman()
