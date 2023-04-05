from termcolor import colored
import time, json


def main():
    print(
        colored(
            "This action is irreversible.  It is recommended to have a copy of the game file before doing this action.  It will reset EVERY bit of gameplay.  Think before doing this.",
            'red'))
    time.sleep(2)
    reset_or_no = str(
        input(colored('Would you like to reset everything?  Y\\N\n>>',
                      'red'))).lower()
    if reset_or_no == 'y':
        int(colored('Deleting Game Save...', 'red'))
        with open('data.json', 'w', encoding='utf-8') as data:
            json.dump("No Save", data)
            time.sleep(2)
            print(colored('Shutting Down Game...', 'red'))
            quit()


if __name__ == '__main__':
    main()
