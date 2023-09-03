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
    def __init__(self, side, event_manager):
        self._characters = []
        self._enhanced_characters = []
        self._side = side
        self.event_manager = event_manager
        self.event_manager.add_listener('character_enhanced', self.on_character_enhanced)
        self.event_manager.add_listener('character_dehanced', self.on_character_dehanced)
        self.event_manager.add_listener('character_died', self.on_character_death)

    @property
    def side(self):
        return self._side

    @property
    def characters(self):
        return self._characters

    @property
    def enhanced_characters(self):
        return self._enhanced_characters

    def on_character_enhanced(self, event):
        if event.data not in self._enhanced_characters:
            self._enhanced_characters.append(event.data)

    def on_character_dehanced(self, event):
        if event.data in self._enhanced_characters:
            self._enhanced_characters.remove(event.data)

    def on_character_death(self, event):
        self.remove_character(event.data)

    def remove_character(self, character):
        if character in self._characters:
            self._characters.remove(character)
        if character in self._enhanced_characters:
            self._enhanced_characters.remove(character)

    def unpack_characters(self, character_list):
        for char in character_list:
            char.event_manager = self.event_manager
            self._characters.append(char)
