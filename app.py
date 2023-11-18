# get a random option from a list of strings
# and print it to the console
import random
# write a do while statement in console
# to keep asking for user input
# until user enters 'exit'
userOp = ''
userPoints = 0
compPoints = 0
while userOp != 'exit':
    options = ['rock', 'paper', 'scissors']
    userOp = input('Enter your option: ')
    if userOp == 'exit':
        print('User points: ', userPoints) 
        print('Computer points: ', compPoints)
        break
    if userOp not in options:
        print('Invalid option')
        continue
    compOp = random.choice(options)
    print('Computer''s option:', compOp)
    
    # if statement to check if user input is valid
    # if not valid, print error message
    # and continue to next iteration
   
    if userOp == 'rock' and compOp == 'scissors':
        print('You win')
        userPoints += 1
    elif userOp == 'rock' and compOp == 'paper':
        print('You lose')
        compPoints += 1
    elif userOp == 'paper' and compOp == 'rock':
        print('You win')
        userPoints += 1
    elif userOp == 'paper' and compOp == 'scissors':
        print('You lose')
        compPoints += 1
    elif userOp == 'scissors' and compOp == 'paper':
        print('You win')
        userPoints += 1
    elif userOp == 'scissors' and compOp == 'rock':
        print('You lose')
        compPoints += 1
    else:
        print('Tie')