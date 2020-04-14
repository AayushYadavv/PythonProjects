import sys
import random
choice = 0
first = int(sys.argv[1])
secound = int(sys.argv[2])
while(True):


    try:
        choice = int(input(f'enter a guess between {first} and {secound}:'))
        syschoice = random.randint(first, secound)
        print(syschoice)

        if(syschoice == choice):
            print('u r genius')
            break
        else:
            print('not in range')
    except ValueError:
        print('Enter a no')
        continue



