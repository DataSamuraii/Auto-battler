
# RPG Auto-battler Documentation

---
# Introduction

Welcome to the epic world of "Battle of the Races"! In this thrilling game, you'll command a squad of valiant warriors, cunning archers, and powerful mages, each belonging to one of four legendary races: Elves, Humans, Orks, or the Undead. Your mission? To lead your squad to victory against a rival faction in a battle where luck will determine the outcome. Will you rise to the challenge and lead your squad to glory?

# Rules

In "Battle of the Races", each game begins with the creation of two opposing squads, each belonging to a specific race. A squad is composed of one mage, three archers, and four warriors. The Elves and Humans form one faction, while the Orks and Undead form the opposing faction.

At the start of the game, two squads are randomly created, each belonging to a specific race. All characters in a squad are divided into two groups: regular and privileged (enhanced). When a character is enhanced, they move to the privileged group, and their damage output increases by 50%.

The order of turns for the races is determined randomly. In one turn, each character in a squad (randomly determined) can perform an action (randomly determined): first from the privileged group, and if it's empty, from the regular group. A privileged group character moves to the general group after performing one action.

# How to Use

To start playing "Battle of the Races", follow these steps:

1. **Initialize the Game**: Run main.py. The game begins by initializing two squads. Each squad is randomly assigned a race (Elves, Humans, Orks, or Undead) and is composed of one mage, three archers, and four warriors.

2. **Start the Battle**: Input 5 in console. The squads are set up automatically. The order of turns for the races is determined randomly.

3. **Win the Game**: The game continues until all characters from one squad are defeated. The remaining squad is declared the winner.

# Script explanation
## main.py

This is the main entry point of the application. It contains the game logic and the main loop.

### Imports

```python
import random
import sys

import Squad
from Fight import Fight
from EventManager import EventManager
from Logger import Logger
```

### Variables

```python
original_stdout = sys.stdout

alliance_factories = [Squad.ElvenCharacterFactory, Squad.HumanCharacterFactory]
horde_factories = [Squad.OrkCharacterFactory, Squad.UndeadCharacterFactory]

event_manager = EventManager()
```

### Functions

- `initialize_squad(faction)`: Initializes a squad for a given faction.
- `print_squad_members(squad)`: Prints the members of a given squad.
- `start_game()`: Starts the game loop.

## Logger.py

This module contains the Logger class, which is used to log messages to a file.

### Class: Logger

- `__init__(self, filename="logfile.txt")`: Constructor. Opens the log file.
- `write(self, message)`: Writes a message to the log file and the standard output.
- `flush(self)`: Flushes the log file and the standard output.

## EventManager.py

This module contains the EventManager class, which is used to manage events in the application.

### Class: EventManager

- `__init__(self)`: Constructor. Initializes the list of listeners.
- `add_listener(self, event_name, listener)`: Adds a listener for a given event.
- `emit(self, event)`: Emits an event to all its listeners.

## Fight.py

This module contains the Fight class, which is used to manage fights between squads.

### Class: Fight

- `__init__(self, squad1, squad2)`: Constructor. Initializes the squads.
- `choose_random_character(self, squad)`: Chooses a random character from a squad.
- `choose_random_action(self, character)`: Chooses a random action for a character.
- `execute_turn(self, attacking_squad, defending_squad)`: Executes a turn in the fight.
- `start_fight(self)`: Starts the fight.

## Squad.py

This module contains the classes related to the creation and management of squads.

### Class: CharacterFactory

This class is used to create characters for a squad.

- `__init__(self, archetypes)`: Constructor. Initializes the archetypes and the quota for each character type.
- `create_character(self, char_type)`: Creates a character of a given type if the quota allows it.
- `create_squad(self)`: Creates a squad with characters according to the quota.

### Class: ElvenCharacterFactory, HumanCharacterFactory, OrkCharacterFactory, UndeadCharacterFactory

These classes inherit from CharacterFactory and are used to create characters of specific races.

### Class: Squad

This class is used to manage a squad.

- `__init__(self, side, event_manager)`: Constructor. Initializes the side, the event manager, and the lists of characters and enhanced characters.
- `on_character_enhanced(self, event)`: Event handler for when a character is enhanced.
- `on_character_dehanced(self, event)`: Event handler for when a character is dehanced.
- `on_character_death(self, event)`: Event handler for when a character dies.
- `remove_character(self, character)`: Removes a character from the squad.
- `unpack_characters(self, character_list)`: Adds a list of characters to the squad.


## Archetypes.py

### Function: enhanced_attack(attack_method)

This function is a decorator that enhances the attack of a character.

### Class: Character

This class is the base class for all characters.

- `__init__(self, name, event_manager=None)`: Constructor. Initializes the name, race, health points, and event manager.
- `enhance(self)`: Enhances the character.
- `take_damage(self, damage)`: Makes the character take damage.
- `death(self)`: Kills the character.

### Race: Elf, Human, Ork, Undead

These classes inherit from Character and are used to create characters of specific races.

### Class: ElvenMage, ElvenArcher, ElvenWarrior, HumanMage, HumanCrossbowman, HumanWarrior, OrkShaman, OrkArcher, OrkWarrior, UndeadNecromancer, UndeadMarksman, UndeadZombie

These classes inherit from their respective race classes and are used to create characters of specific types. Each class has its own unique abilities and actions, such as enhancing other characters, performing magic attacks, shooting, and melee attacks.

# Support and Contributions
Feel free to open an issue or submit a pull request if you find a bug or have suggestions for improvements.