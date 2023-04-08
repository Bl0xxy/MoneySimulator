from termcolor import colored
import time, os

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")

def multiplier_pricing(stats):
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
    print(colored("*Press ENTER to Leave Shop*\n", "red"))
    print(colored("Upgrades:\n", "blue"))
    print(colored("Multiplier: $" + str(int(stats["multiplierprice"])), "green"))

    if stats['multiplier'] > 14:
        print(colored("Super Multiplier: $" + str(int(stats["multiplierprice"]) * 3)))

    if not stats["cmd_shorten"]:
        print(colored("Command Shortener: $75", "green"))


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
    clr_display()


if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")
