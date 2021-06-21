from visualizer import displayResults
from player import Player
from board import streets
from tqdm import tqdm

#matplotlib.use('Agg')

rolls = int(input("How many rolls? "))
sims = int(input("How many simulations? "))

for j in tqdm(range(sims)):
    p = Player()
    for i in range(rolls):
        p.rollDice()

results = []
for s in streets:
    print(s.name, '\t\t', s.visits)
    results.append(s.visits)

displayResults(results)