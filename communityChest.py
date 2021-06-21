from random import randint
from streetNames import StreetNames
from street import Street

class CommunityChest(Street):
    def getPlayerPosition(self):
        cardDrawn = randint(1,16)
        if cardDrawn == 1:
            return StreetNames.GO.value
        elif cardDrawn == 2:
            return StreetNames.JAIL.value
        else:
            return self.index

if __name__ == "__main__":
    c = CommunityChest(StreetNames.COMMUNITY_CHEST_0)
    print(c.index)
    print(c.getPlayerPosition())