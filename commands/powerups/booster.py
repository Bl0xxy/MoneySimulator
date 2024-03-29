from termcolor import colored
import os
import time

def clr_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(stats):
    clr_display()
    if stats['BoosterTotal'] > 5:
        print(colored("You've made the maximum amount of boosters in this playthrough!  Use your shards for other purposes!", "red"))
        time.sleep(1.75)
        return
    if stats['inventory']['boost']:
        stats['moneyamount'] *= 2
        stats['inventory']['boost'] -= 1
        print(colored("Your Money Has Been Doubled!", "green"))
    else:
        print(colored("You don't have any boosters to use!", "red"))
        
    input("\nPress ENTER to Continue... ")

if __name__ == "__main__":
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")