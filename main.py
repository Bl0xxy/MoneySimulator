### IMPORTS ###

from commands import save, money, restart
from termcolor import colored
import os, time, json

### VARIABLES ###

# Lists
cmds = ["money", "cmds", "quit", "shop", "afk", "save", "restart"]
upgrades = ["Multiplier", "Workers", "Workerupgrades"]
upgrades_b = ['multiplier', 'workers', 'workerupgrades']

# Timing Setup
predelaytime = time.time()

# Dictionaries
stats = {}

# Check for save file and save to variables
with open("data.json", encoding="utf-8") as file:
    if not (json.load(file) == "No Save"):
        with open('data.json', encoding='utf-8') as data:
            stats = json.load(data)
    else:
        stats = {
            "multiplier": 1,
            "moneyamount": 0,
            "workers": 0,
            "workerslevel": 0,
            "multiplierpricer": 1,
            "multiplierlevel": 1,
        }
        stats['multiplierprice'] = stats["multiplierpricer"] * 10

# Set other variables
gain = 1 * stats["multiplier"]
stats["multiplierprice"] = stats["multiplierpricer"] * 10
workergain = 1
workerdelay = 1
workerprice = 75

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

    def buy(self):
        stats["moneyamount"] -= stats["multiplierprice"]
        stats[self.name] += 1

    def use(self):
        if self.action != None:
            self.action()
        else:
            raise NoUseShopItem('Item "' + self.name +
                                '" does not have an action assigned to it.')


shopList = colored(f'''


''')

ShopMultiplier = ShopItem("multiplier", "Money Multiplier")

### FUNCTIONS ###


def clr_display():
    os.system('cls' if os.name == 'nt' else 'clear')


def multiplier_pricing():
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


def cmdrun(cmd):  # New Command System
    if (cmd == 'money') or (cmd == 'm'):
        money.main(stats)
    elif cmd == "devcheats":
        stats['moneyamount'] += 1000000
    elif cmd == "quit":
        with open('data.json', 'w') as data:
            json.dump(stats, data)
        quit()
    elif cmd == 'cmds':
        clr_display()
        print(colored("All Current Commands: ", 'yellow'))
        print(' - '.join(cmds))
        time.sleep(5)
        return

    elif cmd == 'save':
        save.main(stats)
    elif cmd == 'restart':
        restart.main()
    elif cmd == 'shop':
        clr_display()
        print(colored("*Press ENTER to Leave Shop*\n", "red"))
        print(colored("Upgrades:\n", "blue"))
        print(
            colored(upgrades[0] + ": $" + str(stats["multiplierprice"]),
                    "green"))

        upgrade = input("\n\n" +
                        colored("Choose an Upgrade\n›› ", "cyan")).lower()
        if upgrade.lower() == "multiplier":
            if stats['multiplierprice'] <= stats["moneyamount"]:
                ShopMultiplier.buy()
                addition = 8.5
                multiplier_pricing()
                stats["multiplierpricer"] += addition
                stats["multiplierprice"] = int(
                    (stats["multiplierpricer"] * stats["multiplierpricer"]) /
                    2)
            else:
                clr_display()
                print(colored("You can't afford that item!  Come back later!"))
                time.sleep(1)
        clr_display()


# Game Launch

# Startup Message
print(colored("To see all commands, use the command \"cmds\"", "yellow"))

time.sleep(1.5)

clr_display()

print(colored('Release 1.6 Soon!', "green"))

time.sleep(1.5)

clr_display()

print(
    colored(
        "Tip: You shouldn't leave the game by pressing stop.  You instead should use the \"quit\" command that is built in!",
        'blue'))

time.sleep(1.5)

clr_display()

# Game Loop
running = True
while running:
    if stats["moneyamount"] <= 0:
        stats['moneyamount'] = 0
    # Get Time
    now = time.time()

    # Display

    print(
        colored(
            f"------Money: {stats['moneyamount']}----Multiplier: x{stats['multiplier']}----",
            "green"))

    command = input(colored("Enter A Command\n›› ", "yellow")).lower()

    if (command in cmds) or command == 'm':
        cmdrun(command.lower())
    clr_display()
