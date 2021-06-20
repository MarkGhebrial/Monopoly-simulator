from player import Player
from board import streets

for j in range(100):
    p = Player()
    for i in range(100):
        p.rollDice()

for s in streets:
    print(s.name, '\t\t', s.visits)