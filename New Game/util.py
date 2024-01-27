### IMPORTS ###

from termcolor import colored
import json, os


def save_game(stats): # Game Save Function
    with open('save.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f)

def clr_display(): # Clear Screen Function
    os.system('cls' if os.name == 'nt' else 'clear')

default = {
        "multiplier": 1,
        "moneyamount": 0,
        "multiplierpricer": 1,
        "multiplierprice": 10,
        "cmd_shorten": False,
        "inventory": {"Mysterious Shard": 0, "Booster": 0, "Iron": 0, "Wood": 0, "Blue Gem": 0},
        "tools": {"Pickaxe": 0, "Sword": 0},
        "BoosterTotal" : 0
        }

info = {

    "name": "Money Simulator",
    "version": "1.8b7",
    "author": "Bl0xxy"

}

game_info = colored(f"{info['name']} {info['version']} by {info['author']}", "magenta", attrs=['bold'])