#I included a dictionary scenarios to store the scenario and choices.
#I've added a design for the complete game, including all possible prompts, choices, and responses.

print("Welcome to the Adventure Game!")
#Choice 1
answer = input ('You are at the crossroad, would you like to go LEFT, RIGHT or FORWARD? ')
if answer.upper() == 'LEFT':
    answer = input ('You encounter a monster, would you like to RUN or ATTACK?')
    if answer.upper() == 'ATTACK':
        answer = input('The monster is armed, do you need a KNIFE or GUN?')
        if answer.upper() == 'KNIFE':
            print("That was not the best idea, sorry you lost!")
        elif answer.upper() == 'GUN':
            print('Aha! brilliant idea, you have killed the monster, you won!')
        else:
            print('please exit!')
    elif answer.upper() == 'RUN':
        answer = input('why choose RUN? Are you not brave enough? Do you wish to CONTINUE or ABORT mission?')
        if answer.upper() == 'CONTINUE':
            answer = input('Nice one! I commend your bravery. Do you want to choose an ARROW or a DAGGER?')
            if answer.upper() == 'ARROW':
                print('Good choice! you have killed the monster. You won!')
            elif answer.upper() == 'DAGGER':
                print('Oh no! the monster has killed you. You lost!')
            else:
                print('You option is invalid')
        elif answer.upper() == 'ABORT':
            print('poor coward, you lost the game')  
        else:
            print('No other option left, please exit')
    else:
            print('invalid option, please exit!')
            
#Choice 2
            
elif answer.upper() == 'RIGHT':
    answer = input('There is a goul-like creature, do you wish to FIGHT or FLEE')
    if answer.upper() == 'FIGHT':
        print('You are so brave! you have killed the goul with the knife you found by your side. congrats!')
    elif answer.upper() == 'FLEE':
        answer = input('why so scared? It is just a game! Do you still want to PLAY or EXIT?')
        if answer.upper() == 'PLAY':
            print('Nice choice! you have a gun! kill the goul!')
            print('Congrats! You have killed it')
        elif answer.upper() == 'EXIT':
            print('sorry coward! try again next time')
        else:
            print('please try again later Thanks!')
    else:
            print('please enter a valid option!')          
#Choice 3
            
elif answer.upper() == 'FORWARD':
    answer = input('This option is boring, do you wish to PROCEED or QUIT?')
    if answer.upper() == 'PROCEED':
        print('It is a lonely path, you are alone in this journey! Mission failed! Try another option')
    elif answer.upper() == 'QUIT':
        answer = input('Okay! Do have a lovely day')
    else:
        print('please leave the game now!')
else:
        print('This is tii bad, Game over!')