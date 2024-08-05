import random
magic_number = random.randint(1, 50)

magic_guess = int(input("what is your lucky guess?"))
guess = -1

while guess != magic_guess:
    guess = int(input("what is your guess?"))
    if guess >= 50:
        print("Goodluck!")
    elif guess <= 30:
        print("You are welcome")
    elif guess >= 10:
        print("OK!")
    else:
        print("You are right!")