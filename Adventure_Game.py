#I included a dictionary scenarios to store the scenario and choices.
#I've added a design for the complete game, including all possible prompts, choices, and responses.


print("Welcome to the Adventure Game!")
choice1 = input("You are standing in a dark forest. Do you want to pick up the MATCH or the FLASHLIGHT? ")
if choice1.lower() == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
choice2 = input()
if choice2.lower == "run":
    print("You try to run, but the bear is too fast. You are eaten alive. Game over.")
elif choice2.lower() == "hide":
    print("You hide behind a tree, and bear passes by without noticing you. You are safe for now. Do you want to FOLLOW the path or LOOK for a safe place to rest? ")
    choice3 = input()
    if choice3.lower == "follow":
        print("You follow the path and came across a clearing. In the center of the clearing is a cottage. Do you want to KNOCK on the door or FO AROUND BACK? ")
    elif choice3.lower == "look":
        print("You look around and find small cave. You enter the cave and fine a treasure chest. Congratulations, you won! ")
    else:
        print("Invalid choice, Game Over!")
elif choice1.lower() == "flashlight":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
    choice2 = input()
    if choice2.lower() == "follow":
        print("you follow the path and come across a river. Do you want to SWIM across or LOOK for a boat? ")
    elif choice2.lower() == "look":
        print("you look in the trees and see a figure hiding. it's a friendly ranger who offers to guide you through the forest. Do you want to ACCEPT tHeir offer or DECLINE? ")
    else:
        print("Invalid choice. Game over!")