### IMPORTS ###

import json
import os

def save_game(stats): # Game Save Function
    with open('game_save.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f)

def clr_display(): # Clear Screen Function
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")