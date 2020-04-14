import sys
import random
choice = 0
first = int(sys.argv[1])
secound = int(sys.argv[2])
while(True):
    
    choice = int(input(print(f'enter a guess between {first} and {secound}:')))
    syschoice = random.randint(first,secound)
    print(syschoice)
    if(syschoice == choice):
        print('U are genius')
        break
    elif(choice>secound or  choice < first):
        print('no. choose not in range')
    else:
        print('wrong choice try again')


