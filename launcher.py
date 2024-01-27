#### IMPORTS ####

from termcolor import colored
import Game, json, util

# Checks The User's Stats for any missing values, then adds the default value of the missing value
def check_stats(stats:dict):

    inventories = []

    old_items = {"Mysterious Shard": "mystshard", "Booster": "boost"}    

    if type(stats) == str or type(stats) == None: # If you don't have a save yet, set it to default
        util.save_game(util.default) 
        return 

    for file in inventories:
        for item in old_items:
            if item in file:
                file[old_items[item]] = file[item]
                file.__delitem__(item)
        for item in util.default:
            if not item in file:
                file[item] = util.default[item]

    for item in old_items: # Name Change Check
        if item in stats:
            stats[old_items[item]] = stats[item]
            stats.__delitem__(item) 

    for item in old_items: # Name Change Check (Inventory)
        if item in stats['inventory']:
            stats['inventory'][old_items[item]] = stats['inventory'][item]
            stats['inventory'].__delitem__(item)

    for item in old_items: # Name Change Check (Tools)
        if item in stats['tools']:
            stats['tools'][old_items[item]] = stats['tools'][item]
            stats['tools'].__delitem__(item)

    for item in util.default: # Main Values Check
        if not item in stats:
            stats[item] = util.default[item]

    for item in util.default['inventory']: # Values Check (Inventory)
        if not item in stats['inventory']:
            stats['inventory'][item] = util.default['inventory'][item]

    for item in util.default['tools']: # Values Check (Tools)
        if not item in stats['tools']:
            stats['tools'][item] = util.default['tools'][item]
    
    
    util.save_game(stats)

def check_file():
    try:
        with open("save.json", encoding="utf-8", mode="r+") as f:
             if f.read() == "":
                f.write("\"No Save\"")
    except FileNotFoundError:
        with open("save.json", encoding="utf-8", mode="w+") as file:
            file.write("\"No Save\"")




def main(): # Main Launcher

    check_file()

    with open("save.json", encoding='utf-8', mode="r") as f:
        stats = json.load(f)
        check_stats(stats)
        
        MoneySim = Game.Game()
        MoneySim.start()
            

if __name__ == '__main__':
    main()
