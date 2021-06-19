import random

class Player:
    def __init__ (self, startingPosition=0):
        self.currentPosition = startingPosition

    def rollDice (self):
        self.currentPosition += random.randint(0, 6) + random.randint(0, 6) # Simulate rolling the dice