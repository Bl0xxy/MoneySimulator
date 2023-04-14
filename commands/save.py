from termcolor import colored
import time, json


def main(data):
    print(colored("Saving Data", 'blue'))
    time.sleep(2)
    with open('game_save.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")
