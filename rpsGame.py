import sys
import random

# Display the initial message
print('ROCK, PAPER, SCISSORS')

# Initialize win, loss, and draw counters
win = 0
loss = 0
draw = 0

# Main game loop
while True:
    # User input loop for choosing a move
    while True:
        # Display current game statistics
        print('%s Wins, %s Losses, %s Ties' % (win, loss, draw))
        print('(r)ock, (p)aper, (s)cissors, (q)uit')
        print('Choose your move: ')
        
        playerMove = str(input())
        
        # Check if the user wants to quit
        if playerMove == 'q':
            sys.exit()
        # Check if the user entered a valid move
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('Please enter r, p, s or q')
    
    # Display user's chosen move
    if playerMove == 'r':
        print('Rock versus.....')
    elif playerMove == 'p':
        print('Paper versus.....')
    elif playerMove == 's':
        print('Scissors versus.....')
    
    # Generate computer's move
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
    
    # Determine the winner and update statistics
    if computerMove == playerMove:
        print('Its a tie')
        draw = draw + 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        print('You Won!')
        win = win + 1
    else:
        print('You Lose!')
        loss = loss + 1