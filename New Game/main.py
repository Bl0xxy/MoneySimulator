# Imports
from SaveFile import SaveFile
from util import default

def main():

    name, version, author = "Money Simulator", "1.8b7", "Bl0xxy"

    # Creates/Loads Save Files
    stats = SaveFile("save", {
        "multiplier": 1, "moneyamount": 0, "multiplierpricer": 1, "multiplierprice": 10, "cmd_shorten": False, "BoosterTotal" : 0
        })
    
    
    inv = SaveFile("inventory", {
        "Mysterious Shard": 0, "Booster": 0, "Iron": 0, "Wood": 0, "Blue Gem": 0, "tool_Pick": 0, "tool_Sword": 0
        })


if __name__ == '__main__':
    main()