### IMPORTS ###

from commands import info, money, quit, restart, save, shop, inventory, craft
from commands.powerups import booster
from termcolor import colored
import command_manager as  cmd_mgr
import json
import util
import time


### VARIABLES ###

stats = {} 


### GAME ###

def run_game():
    global stats
    util.clr_display()
 
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

        util.clr_display()

        # Prevention of Bugs
        if stats["moneyamount"] <= 0: stats['moneyamount'] = 0 
        if stats["multiplier"] < 1: stats["multiplier"] = 1

        # Display
        print(colored(f"------Money: {int(stats['moneyamount'])}----Multiplier: x{int(stats['multiplier'])}------","green"))

        # User Commands & AutoSave
        command = input(colored("Enter A Command\n›› ", "yellow")).lower() 

        command_results = cmd_mgr.main(command.lower(), stats)

        if command_results == "MysteriousShard":
            util.clr_display()
            print(colored("You Found a ", "yellow") + colored("Mysterious Shard", "magenta", attrs=["bold"]) + colored("!", "yellow"))
            stats['inventory']['Mysterious Shard'] += 1
            time.sleep(2.25)
            input("\nPress ENTER to Continue... ")
        util.save_game(stats)


if __name__ == "__main__":
    run_game()
