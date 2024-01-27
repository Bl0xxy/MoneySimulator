from termcolor import colored
import os, time, util

def clr_display():
    os.system("cls" if os.name == "nt" else "clear")

def cmd_list():
    print(colored("Money Simulator Commands", 'yellow'))
    print(f"""

    {colored("* GAMEPLAY *", "cyan")}
    {colored("money", "yellow")} : {colored("Gives you money based on your multiplier", "yellow")}

    {colored("shop", "yellow")} : {colored("Open the shop to buy upgrades!", "yellow")}

    {colored("craft", "yellow")} : {colored("Craft Items In Your Inventory To Make Powerups And Tools!", "yellow")}
    {colored("inventory", "yellow")} : {colored("Look At Your Inventory And Current Tool", "yellow")}
    {colored("booster", "yellow")} : {colored("Multiplies Your Money Total By Two If You Have A Booster", "yellow")}
            

    {colored("* MISC *", "cyan")}
    {colored("help", "yellow")} : {colored("Brings Up Help Menu", "yellow")}                


    {colored("* GAME FILE *", "cyan")}
    {colored("reset", "yellow")} : {colored("Reset Game Save And Start Fresh", "yellow")}
    {colored("leave", "yellow")} : {colored("Saves Game And Leaves", "yellow")}
    {colored("save", "yellow")} : {colored("Saves Game File Manually", "yellow")}

    {colored("* DEVELOPER TESTING COMMANDS *", "blue")}

    {colored("devcheats", "red")} : {colored("Gives you a large amount of money for testing purposes, disabled in GitHub/Replit releases!", "red")}
    """)
    time.sleep(2)
    input(colored("\nPress ENTER To Return to Help Menu\n›› ", "green"))

def shop_help():
    print(f"""
    {colored('Shop Help', "green", attrs=['bold'])}
        {colored('(Type Shop To Enter Shop, Then Select Shop Mode)', "green")}
        {colored('Multiplier: Increases Money Income', "green")}
        {colored('Super Multiplier: Buys 5 Multipliers For The Current Price Of 3 (Unlocked At Multiplier x15)', "green")}

        {colored('Command Shortener: You Can Enter "M" As An Alias To Speed Up Production', "cyan")}

        {colored('You Can Sell Your Items For Differing Prices', "green")}

    """)
    time.sleep(2)
    input(colored("\nPress ENTER To Return to How-To Menu\n›› ", "green"))
    
def crafting_help():
    print(f"""

    {colored('Items and Crafting', "blue", attrs=['bold'])}

    {colored('Every Time You Gain Money, There Is A Chance That You Will Get An Item', "green")}
    {colored("Some Items Are Craftable Allowing You To Craft Powerups And Tools", "green")}
    {colored('You Can Sell Items To Make Money (More Information in "Shop Help")', "green")}
            
    {colored('Some Items Have Crafting Limits', "green")}

    {colored("1. You Can Only Craft 5 Boosters Total Per Playthrough", "red", attrs=['bold'])}
    {colored("2. To Craft A Tool, You Must Craft Each Tier In Order To Make The Next", "red", attrs=['bold'])}

    """)
    time.sleep(2)
    input(colored("\nPress ENTER To Return to How-To Menu\n›› ", "green"))

def beginner_help():
    print(f"""
            {colored("Starting The Game", "yellow")}

            {colored('Enter "Money" To Gain Money', "green")}
            
            {colored('Once You Have Earned 10 Money, Go To The Shop By Entering "Shop" On Your Keyboard', "cyan")}
            {colored('After Entering The Shop, Enter "Buy" To Enter Buy Mode', "green")}
            
            {colored('Enter "Multiplier" To Buy A Multiplier', 'green')}
            {colored('Your Income Has Increased!  Continue This To Get More Money', 'green')}

            {colored('If You Get 75 Money, You Can Buy A Command Shortener To Type "M" Instead of "Money"', 'green')}
            
            """)
    time.sleep(2)
    input(colored("\nPress ENTER To Return to How-To Menu\n›› ", "green"))

def game_credits():
    print(colored("Money Simulator Credits\n", 'yellow'))
    print(colored("Bl0xxy - Developer", "yellow"))

    time.sleep(2)
    input(colored("\nPress ENTER To Return to Help Menu\n›› ", "green"))

def main():
    while True:
        clr_display()
        info = input(f"""
    {util.game_info()}


        {colored("What would you like to get information on?", "yellow")} 

        {colored("A", "green")} - {colored("In-Game Commands", "cyan")}
        {colored("B", "green")} - {colored("How to Play", "cyan")}
        {colored("C", "green")} - {colored("Credits", "cyan")}

        {colored("D", "green")} - {colored("Return to Game", "cyan")}

{colored("›› ", "yellow")}""").lower()

        clr_display()
        
        if info in ["a", "commands", "ingame commands", "in-game commands", "ingamecommands"]:
            cmd_list()
        elif info in ["b", "howto", "how to", "how to play", "how play", "play"]:
            
            while True:
                help = input(f"""
        {colored("What Would You Like To Learn?", "yellow")} 

        {colored("A", "green")} - {colored("Starting The Game", "cyan")}
        {colored("B", "green")} - {colored("Shop Help", "cyan")}
        {colored("C", "green")} - {colored("Items and Crafting", "cyan")}
        {colored("D", "green")} - {colored("(Coming Soon)", "cyan")}

        {colored("E", "green")} - {colored("Return to Help Menu", "cyan")}

{colored("›› ", "yellow")}""").lower()
                
                clr_display()

                if help in ['a', 'start', 'starting the game', 'starting game']:
                    beginner_help()
                elif help in ['b', 'shop help', 'shop', 'shop tutorial', 'shophelp']:
                    shop_help()
                elif help in ['c', 'items', 'crafting', 'items and crafting']:
                    crafting_help()
                elif help in ['e', 'return', 'return to help menu', 'help menu']:
                    break

                clr_display()      

        elif info in ["c", "credits", "gamecredits", "game credits"]:
            game_credits()
        elif info in ["d", "leave", "return", "return game", "return to game", "returngame", "returntogame", "quit", "exit"]:
            break
    
    time.sleep(1)



if __name__ == '__main__':
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")
