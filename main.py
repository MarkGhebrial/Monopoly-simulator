from player import Player
from board import streets

rolls = int(input("How many rolls? "))
sims = int(input("How many simulations? "))

for j in range(sims):
    p = Player()
    for i in range(rolls):
        p.rollDice()

for s in streets:
    print(s.name, '\t\t', s.visits)