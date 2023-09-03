import random
import EventManager


def enhanced_attack(attack_method):
    def wrapper(self, target):
        print(f'{self} is attacking {target}.')
        damage = attack_method(self, target)
        if self.is_enhanced:
            print(f'{self} has enhanced damage.')
            damage *= 1.5
            self.is_enhanced = False
        target.take_damage(damage)
    return wrapper


class Character:
    def __init__(self, name, death_callback=None, event_manager=None):
        self.name = name
        self.race = "Unknown"
        self.hp = 100
        self.death_callback = death_callback
        self._is_enhanced = False
        self.event_manager = event_manager

    def __str__(self):
        return f'{self.name}, the {self.race}'

    def __repr__(self):
        return self.__str__()

    @property
    def is_enhanced(self):
        return self._is_enhanced

    @is_enhanced.setter
    def is_enhanced(self, value):
        if value and not self._is_enhanced:
            self.event_manager.emit(EventManager.CharacterEnhancedEvent(self))
        elif not value and self._is_enhanced:
            self.event_manager.emit(EventManager.CharacterDehancedEvent(self))
        self._is_enhanced = value

    def enhance(self):
        print(f'{self} has been enhanced')
        self._is_enhanced = True
        self.event_manager.emit(EventManager.CharacterEnhancedEvent(self))

    def take_damage(self, damage):
        print(f'{self} has taken {damage} damage.')
        self.hp -= damage
        if self.hp <= 0:
            self.death()

    def death(self):
        print(f'{self} has died!')
        if self.death_callback:
            self.death_callback(self)


class Elf(Character):
    names = [
        "Aranion", "Baelenorn", "Calanon", "Dagorhir", "Erevan", "Fëanor", "Gildor",
        "Haldir", "Iliyanbruen", "Jhaeros", "Kethryll'ia", "Liriel", "Morgath",
        "Narbondel", "Orodreth", "Pharaun", "Qilué", "Rizolvir", "Solas", "Talathel",
        "Umbra", "Vhaerun", "Xiloscient", "Yathlanae", "Zephyrus"
    ]

    def __init__(self):
        chosen_name = random.choice(Elf.names)
        super().__init__(chosen_name)
        self.race = 'elf'


class ElvenMage(Elf):
    def __init__(self):
        super().__init__()
        self.magic_damage = 10

    def action_enhance(self, target):
        target.enhance()

    @enhanced_attack
    def action_magic_attack(self, target):
        return self.magic_damage


class ElvenArcher(Elf):
    def __init__(self):
        super().__init__()
        self.range_damage = 7
        self.melee_damage = 3

    @enhanced_attack
    def action_shoot(self, target):
        return self.range_damage

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class ElvenWarrior(Elf):
    def __init__(self):
        super().__init__()
        self.melee_damage = 15

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class Human(Character):
    names = [
        "Aaron", "Brandon", "Caleb", "Daniel", "Evan", "Frederick", "Gavin",
        "Henry", "Isaac", "Jacob", "Kevin", "Lucas", "Marcus", "Nicholas",
        "Oliver", "Peter", "Quentin", "Richard", "Samuel", "Thomas", "Uriel",
        "Vincent", "William", "Xavier", "Zachary"
    ]

    def __init__(self):
        chosen_name = random.choice(Human.names)
        super().__init__(chosen_name)
        self.race = 'human'


class HumanMage(Human):
    def __init__(self):
        super().__init__()
        self.magic_damage = 4

    def action_enhance(self, target):
        target.enhance()

    @enhanced_attack
    def action_magic_attack(self, target):
        return self.magic_damage


class HumanCrossbowman(Human):
    def __init__(self):
        super().__init__()
        self.range_damage = 5
        self.melee_damage = 3

    @enhanced_attack
    def action_shoot(self, target):
        return self.range_damage

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class HumanWarrior(Human):
    def __init__(self):
        super().__init__()
        self.melee_damage = 18

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class Ork(Character):
    names = [
        "Brag", "Brox", "Brush", "Bugbear", "Croak", "Fomo", "Fungo", "Garish",
        "George Orcwell", "Gerd", "Giltil", "Gnurk", "Gruff", "Grumpy", "Grunt",
        "Moth", "Nerd", "Nut", "Olm", "Orca", "Orcenstein", "Puh", "Rarro", "Rax",
        "Tassu", "Tax", "Tuh", "Unlaylay", "Viagraath", "Wax", "Win", "Wizard"
    ]

    def __init__(self):
        chosen_name = random.choice(Ork.names)
        super().__init__(chosen_name)
        self.race = 'ork'


class OrkShaman(Ork):
    def __init__(self):
        super().__init__()
        self.magic_damage = 7

    def action_enhance(self, target):
        target.enhance()

    @enhanced_attack
    def action_magic_attack(self, target):
        return self.magic_damage


class OrkArcher(Ork):
    def __init__(self):
        super().__init__()
        self.range_damage = 3
        self.melee_damage = 2

    @enhanced_attack
    def action_shoot(self, target):
        return self.range_damage

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class OrkWarrior(Ork):
    def __init__(self):
        super().__init__()
        self.melee_damage = 20

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class Undead(Character):
    names = [
        "Maggot", "Crowrot", "Decay", "Elegy", "Crypt", "Graves", "Ash", "Mort",
        "Mortis", "Morty", "Mortimer", "Necros", "Styx", "Vulture", "Effigy",
        "Cephalophore", "Sepulchre", "Epitaph", "Deeprot", "Repose", "Atropos",
        "Desiccation", "Shi", "D.K.", "Blöt", "Thanatos", "Foulgarb", "Grim"
    ]

    def __init__(self):
        chosen_name = random.choice(Undead.names)
        super().__init__(chosen_name)
        self.race = 'undead'


class UndeadNecromancer(Undead):
    def __init__(self):
        super().__init__()
        self.magic_damage = 5

    def action_enhance(self, target):
        target.enhance()

    @enhanced_attack
    def action_magic_attack(self, target):
        return self.magic_damage


class UndeadMarksman(Undead):
    def __init__(self):
        super().__init__()
        self.range_damage = 4
        self.melee_damage = 2

    @enhanced_attack
    def action_shoot(self, target):
        return self.range_damage

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage


class UndeadZombie(Undead):
    def __init__(self):
        super().__init__()
        self.melee_damage = 18

    @enhanced_attack
    def action_melee_attack(self, target):
        return self.melee_damage
