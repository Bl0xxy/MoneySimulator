from termcolor import colored
import util
import os
import time

names = {"mystshard": "Mysterious Shard", "bluegem": "Blue Gem", "wood": "Wood", "iron": "Iron", "boost":"Boost"}

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")

def inv_empty(stats): # Check Inventory
    for item in stats['inventory']:
        if stats['inventory'][item] != 0:
            print(stats['inventory'][item])
            return False
    return True

def get_item(stats, results):
    item = ""

    if results == "iron" or results == "wood":
        item = colored(results.capitalize(), "white")
    elif results == "mystshard":
        item = colored("a ", "yellow") + colored("Mysterious Shard", "magenta", attrs="bold") 
    elif results == "bluegem":
        item = colored("a ", "yellow") + colored("Blue Gem", "blue", attrs=["bold"])

    util.clr_display()
    print(colored("You Found ", "yellow") + item + colored("!", "yellow"))
    stats['inventory'][results] += 1
    time.sleep(2.25)
    input("\nPress ENTER to Continue...")

    util.save_game(stats)

def print_inventory(stats):
    if inv_empty(stats):
        clr_display()
        print(colored("Your Inventory is Empty!", "yellow"))
        time.sleep(2)
        return

    clr_display()
    
    print(colored("-- Inventory --\n", "green"))

    for item in stats['inventory']:
        print(colored(names[str(item)], "green") + colored(" x" + str(stats['inventory'][item]), "yellow"))

def main(stats):
    print_inventory(stats)
    time.sleep(0.75)
    input("\nPress ENTER to Continue...")


if __name__ == '__main__':
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")