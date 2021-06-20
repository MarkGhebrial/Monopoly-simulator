from streetNames import StreetNames

class Street:
    def __init__ (self, index):
        self.name = StreetNames(index)
        self.index = index.value
        self.visits = 0

    # If the street is special, like chance or community chest, send the player somewhere else
    def getPlayerPosition (self):
        return self.index

    def incrementVisits (self):
        self.visits += 1

    def getVisits (self):
        return self.visits

if __name__ == "__main__":
    s = Street(0)
    print(s.name)