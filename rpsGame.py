import sys
import random

print('ROCK, PAPER, SCISSORS')
win = 0
loss = 0
draw = 0

while True:
    while True:
        print('%s Wins, %s Losses, %s Ties' % (win, loss, draw))
        print('(r)ock, (p)aper, (s)cissors, (q)uit')
        print('Choose your move: ')
        playerMove = str(input())
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('Please enter r, p, s or q')
    #printing user's choice
    if playerMove == 'r':
        print('Rock versus.....')
    elif playerMove == 'p':
        print('Paper versus.....')
    elif playerMove == 's':
        print('Scissors versus.....')
    #choosing the move of computer
    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('Rock')
    elif computerMove == 2:
        computerMove = 'p'
        print('Paper')
    elif computerMove == 3:
        computerMove = 's'
        print('Scissors')
    #determining who is the winner
    if computerMove == playerMove:
        print('Its a tie')
        draw = draw + 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        print('You Won!')
        win = win + 1
    else:
        print('You Lose!')
        loss = loss + 1