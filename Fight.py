import random


class Fight:
    def __init__(self, squad1, squad2):
        self.squad1 = squad1
        self.squad2 = squad2
        self.characters1 = self.squad1.characters
        self.characters2 = self.squad2.characters
        self.enhanced_characters1 = self.squad1.enhanced_characters
        self.enhanced_characters2 = self.squad2.enhanced_characters

    def choose_random_character(self, squad):
        return random.choice(squad)

    def choose_random_action(self, character):
        available_actions = [method for method in dir(character) if method.startswith('action_')]
        if available_actions:
            return getattr(character, random.choice(available_actions))
        return None

    def execute_turn(self, attacking_squad, defending_squad):
        attackers = attacking_squad.characters
        defenders = defending_squad.characters
        temp_char_storage = []
        while attackers and defenders:
            enhanced_attackers = attacking_squad.enhanced_characters
            if enhanced_attackers:
                attacker = self.choose_random_character(enhanced_attackers)
            else:
                attacker = self.choose_random_character(attackers)
                attackers.remove(attacker)
                temp_char_storage.append(attacker)
            attack = self.choose_random_action(attacker)
            if attack:
                if attack.__func__.__name__ == "action_enhance":
                    print(f'{attacker} uses enhance')
                    if attackers:
                        defender = self.choose_random_character(attackers)
                    else:
                        defender = self.choose_random_character(temp_char_storage)
                else:
                    defender = self.choose_random_character(defenders)
                attack(defender)
        attackers.extend(temp_char_storage)

    def start_fight(self):
        while self.characters1 and self.characters2:
            if random.choice([True, False]):
                self.execute_turn(self.squad1, self.squad2)
            else:
                self.execute_turn(self.squad2, self.squad1)
        if self.characters1:
            return f"{self.squad1.side} wins!"
        else:
            return f"{self.squad2.side} wins!"
