#building a Word puzzle game
#CSC 110 BYU-IDAHO

import re
print("Welcome to word guessing game!")

secret = "Jeremiah"
user_guesses = ''
guess_count = 0
hint =' _ ' *len(secret)

print(f"Your hint is: {hint}")
while secret != user_guesses:
    user_guesses = input("please what is your guess? ").lower()
    guess_count += 1
    if secret == user_guesses:
        print("Congratulations! you guessed it!")
        print(f"it took you {guess_count} number of guesses.")
    elif len(secret) != len(user_guesses):
        print("sorry! you guess must have the same letter as the number of word")
    else:
        print("Your guess was incorrect!")
        print(f"your hint is {hint}")
        for index, letter in enumerate(user_guesses):
            if user_guesses[index] == secret[index]:
                print(letter.upper(), end= '')
            elif letter in secret:
                print(letter.lower(), end= '')
            else:
                print('_', end='')