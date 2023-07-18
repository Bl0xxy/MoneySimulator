#### IMPORTS ####

from termcolor import colored
import main as game
import json
import util


# Checks The User's Stats for any missing values, then adds the default value of the missing value
def check_stats(stats):

    default = {
        "multiplier": 1,
        "moneyamount": 0,
        "multiplierpricer": 1,
        "multiplierprice": 10,
        "cmd_shorten": False,
        "inventory": {"Mysterious Shard": 0, "Booster": 0},
        "BoosterTotal" : 0
        }

    if type(stats) == str: stats = default # If you don't have a save yet, set it to default
    elif type(stats) == None: stats = default

    for item in default: # Main Values Check
        if not item in stats:
            stats[item] = default[item]

    for item in default['inventory']: # Inventory Values Check
        if not item in stats['inventory']:
            stats['inventory'][item] = default['inventory'][item]
    
    
    util.save_game(stats)



def main(): # Main Launcher
    try:
        with open("game_save.json", encoding="utf-8", mode="r+") as f:
             if f.read() == "":
                f.write("\"No Save\"")
        with open("game_save.json", encoding="utf-8", mode="r+") as file:

            stats = json.load(file)
            check_stats(stats)
            util.save_game(stats) # Save The Game to Keep The Checked Stats
            game.run_game()
    except FileNotFoundError:
        file = open("game_save.json", encoding="utf-8", mode="w+")
        file.write("\"No Save\"")
        file.close()

        with open("game_save.json", encoding="utf-8", mode="r+") as file:

            stats = json.load(file)
            check_stats(stats)
            util.save_game(stats) # Save The Game to Keep The Checked Stats
            game.run_game()
            

if __name__ == '__main__':
    util.clr_display()
    main()
