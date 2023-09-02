import random
from Fight import Fight
import Squad


alliance_factories = [Squad.ElvenCharacterFactory, Squad.HumanCharacterFactory]
horde_factories = [Squad.OrkCharacterFactory, Squad.UndeadCharacterFactory]

alliance_chosen_races = random.sample(alliance_factories, 1)
horde_chosen_races = random.sample(horde_factories, 1)


alliance_squad = Squad.Squad("Alliance")
for factory_class in alliance_chosen_races:
    factory = factory_class()
    alliance_squad.unpack_characters(factory.create_squad())

horde_squad = Squad.Squad("Horde")
for factory_class in horde_chosen_races:
    factory = factory_class()
    horde_squad.unpack_characters(factory.create_squad())


fight = Fight(alliance_squad, horde_squad)
result = fight.start_fight()
print(result)
