from commands import money, inventory, shop, craft, info, save, restart
from commands.powerups import booster
import util

def main(command, stats):
    # Gameplay Commands
    if command in ["money", "m"]:
        if (command == "m"):
            if stats["cmd_shorten"]:
                if money.main(stats) == "MysteriousShard":
                    return "MysteriousShard"
            else:
                return
        else:
            if money.main(stats) == "MysteriousShard":
                return "MysteriousShard"
        
    elif command == 'shop':
        shop.main(stats)
        return "Normal"
    
    elif command == 'inventory':
        inventory.main(stats)
    
    elif command == "craft":
        craft.main(stats)

    elif command == "booster" or command == "boost":
        util.clr_display()
        booster.main(stats)
    
    # Save File Commands
    elif command == "quit":
        quit.main(stats)
    elif command in ['commands', 'help', 'info', 'cmds', 'cmd']:
        info.main()
        return "Normal"
    elif command in ['save', "saveall", "save-all", "save game", "savegame", "gamesave", "game save"]:
        save.main(stats)
        return "Normal"
    elif command in ['restart', "reset", "delete game save", "delete gamesave", "deletegamesave"]:
        restart.main()
        return "Normal"

    # Developer Testing Commands - Disabled in Releases
    #
    elif command == "devcheats":
        stats['moneyamount'] += 1000000
    #