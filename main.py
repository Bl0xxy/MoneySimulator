### IMPORTS ###

from termcolor import colored, COLORS
from commands.inventory import get_item
import command_manager as cmd_mgr
import launcher
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
                "inventory": {"mystshard": 0, "boost": 0, "iron": 0, "wood": 0, "bluegem": 0},
                "BoosterTotal" : 0
                }

            print(colored('Enter "Help" to Learn How to Play Money Simulator!', "yellow"))

            time.sleep(2)

    while True:  # Loop Game

        util.clr_display()

        # Prevention of Bugs
        if stats["moneyamount"] <= 0: stats['moneyamount'] = 0
        if stats["multiplier"] < 1: stats["multiplier"] = 1

        # Display
        print(colored(f"------Money: {int(stats['moneyamount'])}----Multiplier: x{int(stats['multiplier'])}------",
                      "green"))

        # User Commands & AutoSave
        command = input(colored("Enter A Command\n›› ", "yellow")).lower()

        results = cmd_mgr.main(command.lower(), stats)

        util.save_game(stats)


        # Item Collection System
        if results != None:
            get_item(stats, results)



if __name__ == "__main__":
   launcher.main()
