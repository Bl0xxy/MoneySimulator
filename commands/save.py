from termcolor import colored
import time
import util


def main(data):
    print(colored("Saving Data", 'blue'))
    time.sleep(2)
    util.save_game()


if __name__ == '__main__':
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")
