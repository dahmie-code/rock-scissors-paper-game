import random


print('Rock, Paper and Scissors Game!')
print('(R) = Rock, (P) = Paper, (S) = Scissors')

player = input('Please Choose a Letter (R, P, S): ')
possible_options = ['R', 'P', 'S']
comp_player = random.choice(possible_options)
print(f'\nYou chose {player}, computer chose {comp_player}')

if player == comp_player:
    print(f'Players selected {player}. Draw!')
elif player == 'R':
    if comp_player == 'S':
        print('Rock beats Scissors. You Won!')
    else:
        print('Paper beats Rock. You Lost!')
elif player == 'S':
    if comp_player == 'P':
        print('Scissors beats Paper. You Won!')
    else:
        print('Rock beats Scissors. You Lost')
elif player == 'P':
    if comp_player == 'R':
        print('Paper beats Rock. You Won!')
    else:
        print('Scissors beats Paper. You Lost!')


