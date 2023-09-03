import random
import sys

import Squad
from Fight import Fight
from EventManager import EventManager
from Logger import Logger


original_stdout = sys.stdout

alliance_factories = [Squad.ElvenCharacterFactory, Squad.HumanCharacterFactory]
horde_factories = [Squad.OrkCharacterFactory, Squad.UndeadCharacterFactory]

event_manager = EventManager()


def initialize_squad(faction):
    if faction == "Alliance":
        factories = alliance_factories
    else:
        factories = horde_factories

    chosen_races = random.sample(factories, 1)
    squad = Squad.Squad(faction, event_manager)
    for factory_class in chosen_races:
        factory = factory_class()
        squad.unpack_characters(factory.create_squad())

    return squad


def print_squad_members(squad):
    for character in squad.characters:
        print(character)


def start_game():
    alliance_squad = initialize_squad("Alliance")
    horde_squad = initialize_squad("Horde")

    filename = 'logfile.txt'

    while True:
        print("\n" + "=" * 50)
        print("Commands:")
        print("=" * 50)
        print("1. Show Alliance Squad")
        print("2. Show Horde Squad")
        print("3. Re-generate Alliance Squad")
        print("4. Re-generate Horde Squad")
        print("5. Start the fight")
        print("6. Exit")
        print("=" * 50)

        choice = input("\nChoose an option: ")

        if choice == "1":
            print('\t '.join(map(str, alliance_squad.characters)))
        elif choice == "2":
            print(horde_squad.characters)
        elif choice == "3":
            alliance_squad = initialize_squad("Alliance")
            print(f'{alliance_squad.side} has been reinitialized')
        elif choice == "4":
            horde_squad = initialize_squad("Horde")
            print(f'{horde_squad.side} has been reinitialized')
        elif choice == "5":
            sys.stdout = Logger("logfile.txt")
            fight = Fight(alliance_squad, horde_squad)
            result = fight.start_fight()
            print(result)
            sys.stdout = original_stdout
            print(f"Logs saved to {filename}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    start_game()
