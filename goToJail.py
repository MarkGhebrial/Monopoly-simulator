from streetNames import StreetNames
from street import Street

class GoToJail(Street):
    def getPlayerPosition(self):
        return StreetNames.JAIL.value
