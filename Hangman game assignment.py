import random

words = ["spiderman", "ironman", "thor", "hulk", "captain"]

word = random.choice(words)
guessed = ""
attempts = 5

print("HANGMAN GAME based on Avengers")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Enter a superhero name: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed += guess
        print("Correct!")
    else:
        guessed += guess
        attempts -= 1
        print("Wrong!")

else:
    print("\nYou lost!")
    print("The word was:", word)
