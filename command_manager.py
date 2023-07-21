from commands import money, inventory, craft, info, save, restart, shop
from commands import quit
from commands.powerups import booster
import launcher
import util

def main(command, stats):
    # Gameplay Commands
    if command == "money" or (command == "m" and stats['cmd_shorten']):
        return money.main(stats)
        
    elif command == 'shop':
        shop.main(stats)
    
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
    elif command in ['save', "saveall", "save-all", "save game", "savegame", "gamesave", "game save"]:
        save.main(stats)
    elif command in ['restart', "reset", "delete game save", "delete gamesave", "deletegamesave"]:
        restart.main()

    # Developer Testing Commands - Disabled in Releases
    #
    #elif command == "devcheats":
    #    stats['moneyamount'] += 1000000
    #

if __name__ == "__main__":
    launcher.main()
