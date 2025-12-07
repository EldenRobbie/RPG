import random
from characters import *
from enemies import *
from clr_screen import *
# print(random.randint(1,6))

def main():
    battle()


def battle():
    print(f"A wild {enemy_1.name} appears!")
    input("")
    clear_screen()
    print(f"{player.name} has {player.hp} HP.")
    input("")
    clear_screen()
    print("What would you like to do?")
    print("1. Attack, 2. Defend, 3. Item, 4. Flee ")
    prompt = input("")
    pmt = prompt.lower()
    
    if pmt == "1" or pmt == "attack":
        print("You attack.")
    
    elif pmt == "2" or pmt == "defend":
        print("You defend.")

    elif pmt == "3" or pmt == "item":
        print("You use an item.")
    
    elif pmt == "4" or pmt == "flee":
        print("You flee.")
    
    else:
        print("That's an invalid input.")


def attack():
    pass

def defend():
    pass

def item():
    pass

main()
