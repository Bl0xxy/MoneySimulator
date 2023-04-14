### IMPORTS ###

from commands import info, money, quit, restart, save, shop, inventory, craft
from commands.powerups import booster
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
                if money.main(stats) == "MysteriousShard":
                    return "MysteriousShard"
            else:
                return
        else:
            if money.main(stats) == "MysteriousShard":
                return "MysteriousShard"
        
    elif command == 'shop':
        shop.main(stats)
        return "Normal"
    
    elif command == 'inventory':
        inventory.main(stats)
    
    elif command == "craft":
        craft.main(stats)

    elif command == "booster" or command == "boost":
        clr_display()
        booster.main(stats)
    
    # Save File Commands
    elif command == "quit":
        quit.main(stats)
    elif command in ['commands', 'help', 'info', 'cmds', 'cmd']:
        info.main()
        return "Normal"
    elif command in ['save', "saveall", "save-all", "save game", "savegame", "gamesave", "game save"]:
        save.main(stats)
        return "Normal"
    elif command in ['restart', "reset", "delete game save", "delete gamesave", "deletegamesave"]:
        restart.main()
        return "Normal"

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
                "inventory": {"Mysterious Shard": 0, "Booster": 0},
                "BoosterTotal" : 0
            }

            print(colored('Enter "Help" to Learn How to Play Money Simulator!', "yellow"))

            time.sleep(2)

    while True: # Loop Game

        clr_display()

        # Prevention of Bugs
        if stats["moneyamount"] <= 0: stats['moneyamount'] = 0 
        if stats["multiplier"] < 1: stats["multiplier"] = 1

        # Display
        print(colored(f"------Money: {int(stats['moneyamount'])}----Multiplier: x{int(stats['multiplier'])}----","green"))

        # User Commands & AutoSave
        command = input(colored("Enter A Command\n›› ", "yellow")).lower() 

        command_results = run_command(command.lower())

        if command_results == "MysteriousShard":
            clr_display()
            print(colored("You Found a ", "yellow") + colored("Mysterious Shard", "magenta", attrs=["bold"]) + colored("!", "yellow"))
            stats['inventory']['Mysterious Shard'] += 1
            time.sleep(2.25)
            input("\nPress ENTER to Continue... ")
        save_game()


if __name__ == "__main__":
    run_game()
