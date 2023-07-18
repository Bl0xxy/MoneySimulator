from termcolor import colored
import time, os
from .inventory import is_empty

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")

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


def main(stats):
    ## SHOP SETUP ##

    shopItems = []


    class NoUseShopItem(Exception):
        pass


    class ShopItem:
        def __init__(self, name, displayName):
            self.name = name
            self.displayName = displayName
            self.action = None
            shopItems.append(self)

        def buy(self, price, increase_amount):
            stats["moneyamount"] -= price
            if increase_amount: stats[self.name] += 1

        def use(self):
            if self.action != None:
                self.action()
            else:
                raise NoUseShopItem('Item "' + self.name +'" does not have an action assigned to it.')


    ShopMultiplier = ShopItem("multiplier", "Money Multiplier")
    SuperMultiplier = ShopItem("supermultiplier", "Super Multiplier")
    CommandShortener = ShopItem("cmdshortener", "Command Shortener")

    clr_display()
    shop_mode = input(colored("Do you want to buy or sell items?\n›› ", "green")).lower()

    if shop_mode == "buy":
        clr_display()
        print(colored("*Press ENTER to Leave Shop*\n", "red"))
        print(colored("Upgrades:\n", "blue"))
        print(colored("Multiplier: $" + str(int(stats["multiplierprice"])), "green"))

        if stats['multiplier'] > 14:
            print(colored("Super Multiplier: $" + str(int(stats["multiplierprice"]) * 3), "green"))

        print(colored("\nCommand Shortener: $75" if not stats["cmd_shorten"] else "\nCommand Shortener: Bought Already!", "yellow"))

        upgrade = input("\n\n" +
        colored("Choose an Upgrade\n›› ", "cyan")).lower()
        if upgrade in ["multiplier", "multiply", "mm", "moneymultiplier", "money multiplier", "multi"]:
            if upgrade != "multiplier" and not stats["cmd_shorten"]:
                return
            if stats['multiplierprice'] <= stats["moneyamount"]:
                ShopMultiplier.buy(stats["multiplierprice"], True)
                addition = 8.5
                multiplier_pricing(stats)
                stats["multiplierpricer"] += addition
                stats["multiplierprice"] = int((stats["multiplierpricer"] * stats["multiplierpricer"]) / 2)
            else:
                clr_display()
                print(colored("You can't afford that item!  Come back later!"))
                time.sleep(1)
        elif stats["multiplier"] > 14 and (upgrade in ["supermulti", "supermultiply", "super multi", "supermultiply", "supermultiplier", "super multiplier"]):
            if (upgrade != "super multiplier" and upgrade != "supermultiplier") and not stats["cmd_shorten"]:
                return
            if stats['multiplierprice'] <= stats["moneyamount"]:
                SuperMultiplier.buy(stats["multiplierprice"] * 3, False)
                stats['multiplier'] += 5
                addition = 8.5
                multiplier_pricing(stats)
                stats["multiplierpricer"] += addition
                stats["multiplierprice"] = int((stats["multiplierpricer"] * stats["multiplierpricer"]) / 2)
            else:
                clr_display()
                print(colored("You can't afford that item!  Come back later!"))
                time.sleep(1)
        elif (not stats["cmd_shorten"]) and (upgrade in ["cmdshorten", "command shortener", "command shorten", "cmd shorten", "cmd shortener", "commandshortener", "cmdshortener", "cmdshorten", "commandshorten"]):
            if 75 <= stats["moneyamount"]:
                CommandShortener.buy(75, False)
                stats["cmd_shorten"] = True
            else:
                clr_display()
                print(colored("You can't afford that item!  Come back later!"))
                time.sleep(1)
    elif shop_mode == "sell" or shop_mode == "sel":
        clr_display()
        if is_empty(stats) or stats['inventory']['Mysterious Shard'] == 0:
            print(colored("You don't have anything to sell!  Come back when you have things to sell!", "red"))
            time.sleep(1)
        else:
            print(colored("You can sell your ", "green") + colored("Mysterious Shards", "magenta", attrs=["bold"]) + colored(" for "+str(stats['multiplier'] * 1000)+" money each!", "green"))
            time.sleep(1)
            
            while True:
                try:
                    sell_amount = int(input(colored("How many do you want to sell?\n›› ", "green")))
                    break
                except ValueError:
                    clr_display()
                    print(colored("Please type a number!", "red"))
                    time.sleep(1)
                    clr_display()

            if sell_amount == 0:
                print(colored("Alright then, see you later!", "cyan"))
                time.sleep(1)
                clr_display()
                return
                
            if stats['inventory']['Mysterious Shard'] >= sell_amount:
                stats['inventory']['Mysterious Shard'] -= sell_amount
                stats['moneyamount'] += (1000 * sell_amount) * stats['multiplier']
                print(colored("Sold " + str(sell_amount) + " for " + str((1000 * sell_amount) * stats['multiplier']) + " money!", "green"))
                time.sleep(2)
                clr_display()
                return
            else:
                print(colored("You don't have that many Mysterious Shards!  Check your inventory to see how many you have.", "red"))
                time.sleep(1.25)
                clr_display()
                return
    clr_display()


if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")