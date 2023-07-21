#### IMPORTS ####

from termcolor import colored
import main as game
import json
import util
import time


# Checks The User's Stats for any missing values, then adds the default value of the missing value
def check_stats(stats):

    old_items = {"Mysterious Shard": "mystshard", "Booster": "boost"}

    default = {
        "multiplier": 1,
        "moneyamount": 0,
        "multiplierpricer": 1,
        "multiplierprice": 10,
        "cmd_shorten": False,
        "inventory": {"mystshard": 0, "boost": 0, "iron": 0, "wood": 0, "bluegem": 0},
        "BoosterTotal" : 0
        }
    

    if type(stats) == str: stats = default; return # If you don't have a save yet, set it to default
    elif type(stats) == None: stats = default; return

    for item in old_items: # Name Change Check
        if item in stats:
            stats[old_items[item]] = stats[item] 

    for item in old_items: # Name Change Check (Inventory)
        if item in stats['inventory']:
            stats['inventory'][old_items[item]] = stats['inventory'][item]
            stats['inventory'].__delitem__(item)

    for item in default: # Main Values Check
        if not item in stats:
            stats[item] = default[item]

    for item in default['inventory']: # Inventory Values Check
        if not item in stats['inventory']:
            stats['inventory'][item] = default['inventory'][item]
    
    
    util.save_game(stats)

def check_file():
    try:
        with open("game_save.json", encoding="utf-8", mode="r+") as f:
             if f.read() == "":
                f.write("\"No Save\"")
    except FileNotFoundError:
        with open("game_save.json", encoding="utf-8", mode="w+") as file:
            file.write("\"No Save\"")




def main(): # Main Launcher

    check_file()

    with open("game_save.json", encoding='utf-8', mode="r") as f:
        stats = json.load(f)
        check_stats(stats)
        util.save_game(stats)
        game.run_game()
            

if __name__ == '__main__':
    util.clr_display()
    main()
