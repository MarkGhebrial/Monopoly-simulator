import random
from board import streets

class Player:
    def __init__ (self, startingPosition=0):
        self.currentPosition = startingPosition

    def rollDice (self):
        self.currentPosition = (self.currentPosition + random.randint(0, 6) + random.randint(0, 6)) % 40 # Simulate rolling the dice
        streets[self.currentPosition].incrementVisits() # Increment the visit count of landed street
        lastPosition = self.currentPosition 

        self.currentPosition = streets[self.currentPosition].getPlayerPosition()
        # If the street caused the plaer to move, then increment the counter of the new street
        if lastPosition != self.currentPosition:
            streets[self.currentPosition].incrementVisits()