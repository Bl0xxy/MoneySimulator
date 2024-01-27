### IMPORTS ###

from termcolor import colored
from commands.inventory import get_item
from commands import CommandManager
import launcher, json, util, time

### GAME ###

class Game:
    def __init__(self):
        with open("save.json", encoding='utf-8') as f: self.stats = json.load(f)
    def start(self):
        util.clr_display()
        print(util.game_info)
        time.sleep(1.5)
        util.clr_display()
        print(colored('Enter "Help" to Learn How to Play Money Simulator!', "yellow"))
        time.sleep(0.75)

        while True:  # Loop Game

            # Display

            util.clr_display()

            # User Commands & AutoSave
            command = input(colored(f"------Money: {int(self.stats['moneyamount'])}----Multiplier: x{int(self.stats['multiplier'])}------",
                        "green") +colored("\nEnter A Command\n›› ", "yellow")).lower()

            results = CommandManager.main(command.lower(), self.stats)

            util.save_game(self.stats)


            # Item Collection System
            if results != None:
                get_item(self.stats, results)

if __name__ == "__main__":
   launcher.main()
