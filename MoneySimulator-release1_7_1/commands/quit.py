import os, json

def main(stats):
    with open('game_save.json', 'w') as data:
        json.dump(stats, data)
        os.system("cls" if os.name == "nt" else "clear")
        quit()
    
if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")
