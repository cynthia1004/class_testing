# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = random.choice(choices)
p2 = random.choice(choices)

#my method:
   
from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = random.choice(choices)
p2 = random.choice(choices)

if p1 == p2:
    print("it's a tie")
elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
    print('player 1 wins')
else:
    print('player 2 wins')
        

# First Try:  Globals
from numpy import random

choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

p1 = random.choice(choices)
p2 = random.choice(choices)
print(f'Player 1: {p1}\nPlayer 2: {p2}')

if beats[p1] == p2:
    print('Player 1 wins!')
elif beats[p2] == p1:
    print('Player 2 wins!')
else:
    print('Tie.')


# Second Try:  Functions
from numpy import random

choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

def find_winner(p1, p2):
    if beats[p1] == p2:
        return 'Player 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins!'
    else:
        return'Tie.'

def readysetgo():
    return random.choice(choices)

def play_once():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'Player 1: {p1}\nPlayer 2: {p2}')

    winner = find_winner(p1, p2)
    print(f'The winner is: {winner}')

play_once()


# Third Try:  Classes
class Player():
    def __init__(self, name, strategy='random'):
        self.name = name
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.strategy = strategy

    def readysetgo(self):
        if self.strategy == 'random':
            return random.choice(self.choices)
        elif self.strategy == 'always_rock':
            return 'rock'

class PlayerAlwaysRock(Player):
    def readysetgo(self):
        return 'rock'

class Game():
    def __init__(self, num_players=2):
        self.beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
        self.num_players = num_players
        self.players = [Player(str(n+1)) for n in range(num_players)]
        # Note: calls Player() class

    def find_winner(self, p1, p2):
        if self.beats[p1] == p2:
            return 'Player 1'
        elif self.beats[p2] == p1:
            return 'Player 2'
        else:
            return'Tie'

    def play_once(self):
        hands = [p.readysetgo() for p in self.players]
        print('Everyone plays:', hands)

        for player, hand in zip(self.players, hands):
            # player = <1>
            # self.players = [<1>, <2>, <3>]
            # hand = 'rock'
            # hands = ['rock', 'paper', 'paper']
            results = [self.find_winner(hand, h) for h in hands]

            wins = sum([r == 'Player 1' for r in results])
            losses = sum([r == 'Player 2' for r in results])
            ties = sum([r == 'Tie' for r in results]) - 1
            print(f'Player {player.name}: {wins} wins, {losses} losses, and {ties} ties.')
            player.wins += wins

game = Game()
game.play_once()

game = Game(num_players=4)
game.play_once()