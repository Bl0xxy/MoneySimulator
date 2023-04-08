### IMPORTS ###

from commands import info, money, quit, restart, save, shop
from termcolor import colored
import os
import json

### SAVE FILE ###

stats = {}

with open("game_save.json", encoding="utf-8") as file:
    if not (json.load(file) == "No Save"):
        with open("game_save.json", encoding="utf-8") as data:
            stats = json.load(data)
    else:
        stats = {
            "multiplier": 1,
            "moneyamount": 0,
            "multiplierpricer": 1,
            "multiplierprice": 10,
            "cmd_shorten": False
        }

### FUNCTIONS ###


def save_game():
    with open('game_save.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f)


def clr_display():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_command(command):
    # Gameplay Commands
    if command in ["money", "m"]:
        if (command == "m"):
            if stats["cmd_shorten"]:
                money.main(stats)
            else:
                return
        else:
            money.main(stats)
    elif command == 'shop':
        shop.main(stats)

    # Save File Commands
    elif command == "quit":
        quit.main(stats)
    elif command in ['commands', 'help', 'info', 'cmds', 'cmd']:
        info.main()
    elif command in [
            'save', "saveall", "save-all", "save game", "savegame", "gamesave",
            "game save"
    ]:
        save.main(stats)
    elif command in [
            'restart', "reset", "delete game save", "delete gamesave",
            "deletegamesave"
    ]:
        restart.main()

    # Developer Testing Commands - Disabled in Releases
    #
    # elif command == "devcheats":
    #    stats['moneyamount'] += 1000000
    #


### GAME ###

clr_display()

while True:  # Loop Game
    if stats["moneyamount"] <= 0:
        stats['moneyamount'] = 0  # Prevention of Bugs

    # Display
    print(
        colored(
            f"------Money: {int(stats['moneyamount'])}----Multiplier: x{int(stats['multiplier'])}----",
            "green"))

    command = input(colored("Enter A Command\n›› ",
                            "yellow")).lower()  # Get Command From User

    run_command(command.lower())  # Run the Given Command

    # AutoSave Feature
    save_game()

    clr_display()  # Updates Display
