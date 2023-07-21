from random import randint

def main(stats):
  stats['moneyamount'] += stats['multiplier']

  if randint(1, 450) == 1:
     return "bluegem"

  if randint(1, 200) == 1:
    return "mystshard"
  
  if randint(1, 50) == 1:
    return "iron"
  
  if randint(1, 15) == 1:
    return "wood"
  

if __name__ == '__main__':
    print("It doesn't work like that!  Try running launcher.py to play Money Simulator!")