from random import randint
from streetNames import StreetNames
from street import Street

class Chance(Street):
    def getPlayerPosition(self):
        cardDrawn = randint(1,16)
        if cardDrawn == 1:
            return StreetNames.READING_RAILROAD.value
        elif cardDrawn == 2:
            return StreetNames.JAIL.value
        elif cardDrawn == 3:
            return (self.index - 3) % 40 # Go back 3 spaces
        elif cardDrawn == 4:
            return StreetNames.ST_CHARLES_PLACE.value
        elif cardDrawn == 5:
            return StreetNames.GO.value
        elif cardDrawn == 6:
            return StreetNames.ILLINOIS_AVENUE.value
        elif cardDrawn == 7:
            return StreetNames.BOARDWALK.value
        elif cardDrawn == 8:
            # Advance to nearest utility
            position = self.index
            while position != StreetNames.ELECTRIC_COMPANY.value | position != StreetNames.WATER_WORKS.value:
                print(position)
                position = (position + 1) % 40
            return position
        elif cardDrawn == 9 | cardDrawn == 10:
            # Advance to nearest railroad
            position = self.index
            while position != StreetNames.READING_RAILROAD.value | position != StreetNames.PENNSYLVANIA_RAILROAD.value | position != StreetNames.BO_RAILROAD.value | position != StreetNames.SHORT_LINE_RAILROAD.value:
                print(position)
                position = (position + 1) % 40
            return position
        else:
            return self.index

if __name__ == "__main__":
    c = Chance(StreetNames.CHANCE_0)
    print(c.index)
    print(c.getPlayerPosition())