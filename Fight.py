import random


class Fight:
    def __init__(self, squad1, squad2):
        self.squad1 = squad1
        self.squad2 = squad2

    def choose_random_character(self, squad):
        return random.choice(squad)

    def choose_random_action(self, character):
        available_actions = [method for method in dir(character) if method.startswith('action_')]
        if available_actions:
            return getattr(character, random.choice(available_actions))
        return None

    def execute_turn(self, attacking_squad, defending_squad):
        temp_char_storage = []
        while attacking_squad:
            attacker = self.choose_random_character(attacking_squad)
            temp_char_storage.append(attacker)
            attack = self.choose_random_action(attacker)
            if attack and defending_squad:
                if attack.__func__.__name__ == "action_enhance":
                    defender = self.choose_random_character(attacking_squad)
                else:
                    defender = self.choose_random_character(defending_squad)
                attack(defender)
            attacking_squad.remove(attacker)
        attacking_squad.extend(temp_char_storage)

    def start_fight(self):
        characters1 = self.squad1.get_characters()
        characters2 = self.squad2.get_characters()
        while characters1 and characters2:
            if random.choice([True, False]):
                self.execute_turn(characters1, characters2)
            else:
                self.execute_turn(characters2, characters1)
        if characters1:
            return f"{self.squad1.side} wins!"
        else:
            return f"{self.squad2.side} wins!"
