from termcolor import colored
import time, json


def main(data):
    print(colored("Saving Data", 'blue'))
    time.sleep(2)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
