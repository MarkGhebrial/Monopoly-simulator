class Street:
    def __init__ (self, name, index):
        self.name = name
        self.index = index
        self.visits = 0

    # If the street is special, like chance or community chest, send the player somewhere else
    def getPlayerPosition (self):
        return self.index

    def incrementVisits (self):
        self.visits += 1

    def getVisits (self):
        return self.visits