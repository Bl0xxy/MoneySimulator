### IMPORTS ###

from commands import info, money, quit, restart, save, shop
from termcolor import colored
import os
import json
import time

stats = {}

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
    elif command == "devcheats":
        stats['moneyamount'] += 1000000
    #


### GAME ###


def run_game():
    global stats
    clr_display()

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
                "cmd_shorten": False,
                "workers": 0
            }

            print(
                colored('Enter "Help" to Learn How to Play Money Simulator!',
                        "yellow"))

            time.sleep(2)

    clr_display()

    while True:  # Loop Game

        # Prevention of Bugs
        if stats["moneyamount"] <= 0: stats['moneyamount'] = 0
        if stats["workers"] <= 0: stats["workers"] = 0
        if stats["workers"] > 5: stats["workers"] = 5
        if stats["multiplier"] > 2: stats["multiplier"] = 1

        # Display
        print(
            colored(
                f"------Money: {int(stats['moneyamount'])}----Multiplier: x{int(stats['multiplier'])}----Workers: {int(stats['workers'])}----",
                "green"))

        # User Commands & AutoSave
        command = input(colored("Enter A Command\n›› ", "yellow")).lower()
        run_command(command.lower())

        save_game()

        clr_display()


if __name__ == "__main__":
    run_game()
