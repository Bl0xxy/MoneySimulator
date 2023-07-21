from termcolor import colored
from commands import inventory as inv
import util
import time

aliases = [["multiplier", "multiply", "mm", "moneymultiplier", "money multiplier", "multi"], ["supermulti", "supermultiply", "super multi", "supermultiply", "supermultiplier", "super multiplier"], ["cmdshorten", "command shortener", "command shorten", "cmd shorten", "cmd shortener", "commandshortener", "cmdshortener", "cmdshorten", "commandshorten"]]

prices = {"bluegem": 10000, "mystshard": 5000, "iron": 150, "wood": 75}

names = {"mystshard": "Mysterious Shard", "bluegem": "Blue Gem", "wood": 0, "iron": 0}

def multiplier_pricing(stats):
    global addition
    if stats["multiplier"] < 6:
        addition = 8.5
    elif stats["multiplier"] < 11:
        addition = 18.5
    elif stats["multiplier"] < 16:
        addition = 24
    elif stats["multiplier"] < 21:
        addition = 63
    elif stats["multiplier"] < 51:
        addition = 100

def buy_item(upgrade, stats):
    shortener = stats['cmd_shorten']
    if upgrade in aliases[0] and shortener or upgrade == "multiplier":
        if stats['moneyamount'] >= stats['multiplierprice']:
            stats['moneyamount'] -= stats['multiplierprice']
            stats['multiplier'] += 1
            multiplier_pricing(stats)
            stats["multiplierpricer"] += addition
            stats["multiplierprice"] = int((stats["multiplierpricer"] * stats["multiplierpricer"]) / 2)
        else:
            util.clr_display()
            print(colored("You can't afford that item!  Come back later!"))
            time.sleep(1)
    elif ((upgrade in aliases[1] and shortener) or upgrade == "supermultiplier" or upgrade == "super multiplier") and stats['multiplier'] > 14:
        if stats['moneyamount'] >= stats['multiplierprice'] * 3:
            stats['moneyamount'] -= stats['multiplierprice'] * 3
            stats['multiplier'] += 5
            multiplier_pricing(stats)
            stats["multiplierpricer"] += addition
            stats["multiplierprice"] = int((stats["multiplierpricer"] * stats["multiplierpricer"]) / 2)
        else:
            util.clr_display()
            print(colored("You can't afford that item!  Come back later!"))
            time.sleep(1)
    elif (shortener and upgrade in aliases[2]) or upgrade == "command shortener" or upgrade == "commandshortener":
        if stats['moneyamount'] >= 75:
            stats['moneyamount'] -= 75
            stats['cmd_shorten'] = True
        else:
            util.clr_display()
            print(colored("You can't afford that item!  Come back later!"))
            time.sleep(1)


def main(stats):

    util.clr_display()

    mode = input(colored("Do you want to buy or sell items?\n›› ", "green")).lower()

    if mode == "buy" or mode == "b":
        util.clr_display()
        print(colored("*Press ENTER to Leave Shop*\n", "red"))
        print(colored("-- Upgrades --\n", "blue"))
        print(colored("Multiplier: $" + str(int(stats["multiplierprice"])), "green"))
        if stats['multiplier'] > 14:
            print(colored("Super Multiplier: $" + str(int(stats["multiplierprice"]) * 3), "green"))

        print(colored("\nCommand Shortener: $75" if not stats["cmd_shorten"] else "\nCommand Shortener: Bought Already!", "yellow"))

        upgrade = input("\n\n" + colored("Choose an Upgrade\n›› ", "cyan")).lower()

        buy_item(upgrade, stats)
    elif mode == "sell" or mode == 's':
        util.clr_display()

        print(colored("-- Inventory --\n", "green"))

        if inv.inv_empty(stats):
            print("(Empty)", "grey")
            input("\nPress ENTER to Continue... ")
            return

        while True:
            inv.print_inventory(stats)
            sell = input(colored('\nWhat Item Would You Like To Sell?\n›› ', "green"))

            if not sell in stats['inventory']:
                continue

            if not sell in stats['inventory']:
                util.clr_display()
                print(colored("You don't have any to sell!", "red"))
                time.sleep(0.75)
                continue

            while True:
                inv.print_inventory(stats)
                try:
                    sell_amt = int(input(colored("\nHow many do you want to sell?\n›› ", "green")))
                    break
                except ValueError:
                    util.clr_display()
                    print(colored("Please type a number!", "red"))
                    time.sleep(1)
            
            if sell_amt == 0:
                return
            
            
            if int(sell_amt) > stats['inventory'][sell]:
                util.clr_display()
                print(colored("You don't have enough!", "red"))
                time.sleep(0.75)
                continue

            name = ""

            if sell_amt > 1 and not (names[sell] == 0):
                name = names[sell]
            else:
                name = str(sell).capitalize()


            stats['moneyamount'] += prices[sell] * stats['multiplier']
            stats['inventory'][sell] -= sell_amt

            util.clr_display()

            print(colored(f"You sold {str(int(sell_amt))} {name} for {prices[sell]*stats['multiplier']}"))

            time.sleep(1.75)
            return


if __name__ == "__main__":
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")