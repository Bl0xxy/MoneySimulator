from termcolor import colored
from random import randint

def main(stats):
  stats['moneyamount'] += stats['multiplier']

  mysterious_shard_randomization = randint(1, 500)

  if mysterious_shard_randomization == 5:
    return "MysteriousShard"

  return "Normal"

if __name__ == '__main__':
    print("It doesn't work like that!  Try running main.py to play Money Simulator!")
