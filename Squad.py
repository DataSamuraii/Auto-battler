import Archetypes


class CharacterFactory:
    def __init__(self, archetypes):
        self.archetypes = archetypes
        self.quota = {
            'mage': 1,
            'archer': 3,
            'warrior': 4
        }

    def create_character(self, char_type):
        if self.quota[char_type] > 0:
            self.quota[char_type] -= 1
            return self.archetypes[char_type]()

    def create_squad(self):
        squad = []
        for char_type, count in self.quota.items():
            for _ in range(count):
                squad.append(self.create_character(char_type))
        return squad


class ElvenCharacterFactory(CharacterFactory):
    def __init__(self):
        super().__init__({
            'mage': Archetypes.ElvenMage,
            'archer': Archetypes.ElvenArcher,
            'warrior': Archetypes.ElvenWarrior,
        })


class HumanCharacterFactory(CharacterFactory):
    def __init__(self):
        super().__init__({
            'mage': Archetypes.HumanMage,
            'archer': Archetypes.HumanCrossbowman,
            'warrior': Archetypes.HumanWarrior,
        })


class OrkCharacterFactory(CharacterFactory):
    def __init__(self):
        super().__init__({
            'mage': Archetypes.OrkShaman,
            'archer': Archetypes.OrkArcher,
            'warrior': Archetypes.OrkWarrior,
        })


class UndeadCharacterFactory(CharacterFactory):
    def __init__(self):
        super().__init__({
            'mage': Archetypes.UndeadNecromancer,
            'archer': Archetypes.UndeadMarksman,
            'warrior': Archetypes.UndeadZombie
        })


class Squad:
    def __init__(self, side):
        self._characters = []
        self.side = side

    def unpack_characters(self, character_list):
        for char in character_list:
            char.death_callback = self.character_death
            self._characters.append(char)

    def remove_character(self, character):
        self._characters.remove(character)

    def character_death(self, character):
        self.remove_character(character)

    def get_characters(self):
        return self._characters