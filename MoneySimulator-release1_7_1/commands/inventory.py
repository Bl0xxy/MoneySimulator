from termcolor import colored
import os
import time

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")

def is_empty(stats):
    if stats['inventory']['Mysterious Shard'] == 0 and stats['inventory']['Booster'] == 0:
        return True
    else:
        return False

def main(stats):

    clr_display()

    if stats['inventory']['Mysterious Shard'] == 0 and stats['inventory']['Booster'] == 0:
        print(colored("Your Inventory is Empty!", "yellow"))
        time.sleep(2)
        return

    if not stats['inventory']['Mysterious Shard'] == 0:
        print(colored("Mysterious Shards: " + str(stats['inventory']['Mysterious Shard']), "green"))
    if not stats['inventory']['Booster'] == 0:
        print(colored("Boosters: " + str(stats['inventory']['Booster']), "green"))

    time.sleep(2)

if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")