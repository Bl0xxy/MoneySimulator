from termcolor import colored
import os, time

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        clr_display()
        info = input(f"""
        {colored("What would you like to get information on?", "yellow")} 

        {colored("A", "green")} - {colored("In-Game Commands", "cyan")}
        {colored("B", "green")} - {colored("How to Play", "cyan")}
        {colored("C", "green")} - {colored("Credits", "cyan")}

        {colored("D", "green")} - {colored("Return to Game", "cyan")}
        """).lower()

        clr_display()
        
        if info in ["a", "commands", "ingame commands", "in-game commands", "ingamecommands"]:
            print(colored("Money Simulator Commands", 'yellow'))
            print(f"""
            {colored("* MISC *", "cyan")}
            {colored("cmds", "yellow")} : {colored("Shows a List of Commands", "yellow")}

            {colored("* GAMEPLAY *", "cyan")}
            {colored("money", "yellow")} : {colored("Gives you money based on your multiplier", "yellow")}
            {colored("m", "yellow")} : {colored("Unlockable shortened command to gain money", "yellow")}

            {colored("shop", "yellow")} : {colored("Open the shop to buy upgrades!", "yellow")}

            {colored("craft", "yellow")} : {colored("Craft your artifacts into power-ups!", "yellow")}
            {colored("inventory", "yellow")} : {colored("Find out how many artifacts and power-ups you have!", "yellow")}
            {colored("booster", "yellow")} : {colored("Multiplies your money by two!  Requires Booster!", "yellow")}
            
                
            {colored("* GAME FILE *", "cyan")}
            {colored("restart", "yellow")} : {colored("Restart your game save, and start fresh!", "yellow")}
            {colored("quit", "yellow")} : {colored("Save, Then Leave the Game", "yellow")}
            {colored("save", "yellow")} : {colored("Saves your game file", "yellow")}

            {colored("* DEVELOPER TESTING COMMANDS *", "blue")}

            {colored("devcheats", "red")} : {colored("Gives you a large amount of money for testing purposes, disabled in GitHub/Replit releases!", "red")}
            """)

            time.sleep(2)
            input(colored("\nPress ENTER To Return to Info Menu\n›› ", "green"))
        elif info in ["b", "howto", "how to", "how to play", "how play", "play"]:
            print(colored("Money Simulator How-To", 'yellow'))
            print(f"""
            {colored('Type "Money" and press enter to gain money!', "green")}
            
            {colored('Once you have 10 money, you can buy a multiplier from the shop!', "cyan")}
            {colored('To buy something in the shop, enter "Shop" and then enter in what you would like to purchase.', "yellow")}

            {colored('Shop Help', "green", attrs=['bold'])}
            {colored('Multiplier: Increases Money Income', "green")}
            {colored('Super Multiplier: Buys 5 multipliers for the price 3 at your current price', "green")}
            
            {colored('Crafting Help', "blue", attrs=['bold'])}
            {colored('There is a small chance you can get a ', "cyan") + colored("Mysterious Shard", "magenta", attrs=["bold"]) + colored(" every time you gain money", "green")}
            {colored('To see how many shards you have, check your inventory by entering "Inventory"')}
            {colored("If you have 25 or more shards, you can combine them to craft a booster!")}
            {colored("Using the booster doubles your money once!")}

            {colored("You can only have crafted 5 boosters throughout your ENTIRE playthrough.", "red", attrs=['bold'])}
            

            {colored('To save your game, enter "Save" and after that, it should save your game file!', "cyan")}
            
            {colored('Your game autosaves every time you run a command!', "cyan")}
            {colored('To reset all your data, enter "reset" or "restart" and enter "y"', "cyan")}
            """)

            time.sleep(2)
            input(colored("\nPress ENTER To Return to Info Menu\n›› ", "green"))
        elif info in ["c", "credits", "gamecredits", "game credits"]:
            print(colored("Money Simulator Credits\n", 'yellow'))
            print(colored("Bl0xxy - Head Developer, Only Developer (Soon to Change)", "yellow"))

            time.sleep(2)
            input(colored("\nPress ENTER To Return to Info Menu\n›› ", "green"))
        elif info in ["d", "leave", "return", "return game", "return to game", "returngame", "returntogame", "quit", "exit"]:
            break
    
    time.sleep(1)



if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")
