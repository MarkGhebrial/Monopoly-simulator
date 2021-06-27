import random
from streetNames import StreetNames
from board import streets

class Player:
    def __init__ (self, startingPosition=0):
        self.currentPosition = startingPosition
        self.doubleRolls = 0

    def rollDice (self):
        # Roll the dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)

        if die1 == die2:
            self.doubleRolls += 1
        else:
            self.doubleRolls = 0

        if self.doubleRolls == 3:
            self.currentPosition = StreetNames.JAIL.value
            streets[StreetNames.JAIL.value].incrementVisits()
            self.doubleRolls = 0
            print("rolled too many doubles")
            return

        self.currentPosition = (self.currentPosition + die1 + die2) % 40 # Advance the player
        streets[self.currentPosition].incrementVisits() # Increment the visit count of landed street
        lastPosition = self.currentPosition 

        self.currentPosition = streets[self.currentPosition].getPlayerPosition()
        # If the street caused the plaer to move, then increment the counter of the new street
        if lastPosition != self.currentPosition:
            streets[self.currentPosition].incrementVisits()

if __name__ == "__main__":
    p = Player(StreetNames.JAIL.value + 1)
    while p.currentPosition != StreetNames.JAIL.value:
        p.currentPosition = 0
        p.rollDice()
        p.rollDice()
        p.rollDice()
        print(p.currentPosition)