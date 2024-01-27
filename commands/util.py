### IMPORTS ###

from termcolor import colored
import json
import os

def save(stats): # Game Save Function
    with open('game_save.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f)

def clr_display(): # Clear Screen Function
    os.system('cls' if os.name == 'nt' else 'clear')

info = {

    "name": "Money Simulator",
    "version": "1.8b7",
    "author": "Bl0xxy"

}

def game_info():
    return colored(f"{info['name']} {info['version']} by {info['author']}", "magenta", attrs=['bold'])


if __name__ == "__main__":
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")