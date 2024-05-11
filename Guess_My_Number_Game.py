import random
magic_number = random.randint(1, 100)

magic_number = int(input("what is your magic number? "))
guess = -1

while guess != magic_number:
    guess = int(input("what is your guess? "))
if guess < magic_number:
    print("Higher")
elif guess > magic_number:
    print("Lower")
else:
    print("You guessed right!")