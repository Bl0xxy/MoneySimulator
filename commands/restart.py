from termcolor import colored
import time, json, os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        colored(
            "This action is irreversible.  It is recommended to have a copy of the game file before doing this action.  It will reset EVERY bit of gameplay.  Think before doing this.",
            'red'))
    time.sleep(2)
    reset_or_no = str(
        input(colored('Would you like to reset everything?  Y\\N\n›› ',
                      'red'))).lower()
    if reset_or_no == 'y':
        print(colored('Deleting Game Save...', 'red'))
        with open('game_save.json', 'w', encoding='utf-8') as data:
            json.dump("No Save", data)
            time.sleep(1.5)
            print(colored('Shutting Down Game...', 'red'))
            time.sleep(1.5)
            os.system("cls" if os.name == "nt" else "clear")
            quit()


if __name__ == '__main__':
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")
