from street import Street
from communityChest import CommunityChest
from chance import Chance
from goToJail import GoToJail
from streetNames import StreetNames

#------------------Create the list of streets---------------#

# Fill the list with normal streets
streets = []
for s in StreetNames:
    streets.append(Street(s))

# Override go to jai
streets[StreetNames.GO_TO_JAIL.value] = GoToJail(StreetNames.GO_TO_JAIL)

# Override the community chests
for i in [StreetNames.COMMUNITY_CHEST_0, StreetNames.COMMUNITY_CHEST_1, StreetNames.COMMUNITY_CHEST_2]:
    streets[i.value] = CommunityChest(i)

# Override the chances
for i in [StreetNames.CHANCE_0, StreetNames.CHANCE_1, StreetNames.CHANCE_2]:
    streets[i.value] = Chance(i)
        
#-----------------------------------------------------------#
