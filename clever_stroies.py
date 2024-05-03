print("Hello user! welcome to the mad lib game")
adjective = input("Please enter adjective: ")
animal= input("please enter name of animal: ")
verb = input("Enter a verb: ")
exclamation = input("please enter exclamation: ")
verb1 = input("please enter verb: ")
verb2 = input("please enter verb: ")

exclamation = exclamation.capitalize()





words = f"""The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb} down the hallway. \n"{exclamation}!" I yelled. But all
I could think to do was to {verb} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb}
right in front of my family."""


print(words)
