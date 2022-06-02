import random

print("ROCK SCISSORS PAPER GAME ")
r = 'Rock'
s = 'Scissors'
p = 'paper'



player_input1 = input("player 1 picks: ")
if player_input1 == 'r':
    print('player 1 picks Rock')
elif player_input1 == 's':
    print('player 1 picks Scissors')
elif player_input1 == 'p':
    print('player 1 picks Paper')
choice = ('Rock', 'Scissors', 'Paper')

computer = random.choice(choice)
print('computer picks: ', computer)
#class player():
    #def player_1(self):


while player_input1 == 'r' and computer == ('Rock'):
    print('The game is a draw.... Try againr')
    player_input1 = input("player 1 picks: ")
    if player_input1 == 'r':
        print('player 1 picks Rock')
    elif player_input1 == 's':
        print('player 1 picks Scissors')
    elif player_input1 == 'p':
        print('player 1 picks Paper')
    choice = ('Rock', 'Scissors', 'Paper')

    computer = random.choice(choice)

    print('computer picks: ', computer)




else:
    if player_input1 == 'r' and computer == 'Scissors':
        print('player 1 wins')
    elif player_input1 == 'r' and computer == 'Paper':
        print('computer wins')

while player_input1 == 's' and computer == ('Scissors'):
    print('The game is a draw.... Try again')
    player_input1 = input("player 1 picks: ")
    if player_input1 == 'r':
        print('player 1 picks Rock')
    elif player_input1 == 's':
        print('player 1 picks Scissors')
    elif player_input1 == 'p':
        print('player 1 picks Paper')
    choice = ('Rock', 'Scissors', 'Paper')

    computer = random.choice(choice)

    print('computer picks: ', computer)




else:
    if player_input1 == 's' and computer == 'Rock':
        print('Computer Wins')
    elif player_input1 == 's' and computer == 'Paper':
        print('Player 1 wins')
while player_input1 == 'p' and computer == ('Paper'):
    print('The game is a draw.... Try again')
    player_input1 = input("player 1 picks: ")
    if player_input1 == 'r':
        print('player 1 picks Rock')
    elif player_input1 == 's':
        print('player 1 picks Scissors')
    elif player_input1 == 'p':
        print('player 1 picks Paper')
    choice = ('Rock', 'Scissors', 'Paper')

    computer = random.choice(choice)

    print('computer picks: ', computer)




else:
    if player_input1 == 'p' and computer == 'Scissors':
        print('Computer wins')
    elif player_input1 == 'p' and computer == 'Rock':
        print('Player 1 wins')






















