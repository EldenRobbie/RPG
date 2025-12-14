import random
from characters import *
from enemies import *
from clr_screen import *

'''
Make items to be used in battle()

Need to keep track of how many items the character has.
'''

# Potion is working as inteded


def main():
    input("We're going to test potions! ")
    clear_screen()
    input(f"{player.name} has {player.hp} health. Their health is full. ")
    clear_screen()
    player.hp -= 3
    print(f"{player.name} takes 3 damage!")
    input(f"They have {player.hp} health.")
    clear_screen()
    potion()
    input("They use a potion.")
    clear_screen()
    print(f"{player.name} has {player.hp} health.")


item_list = {"potion": 1}


def items():
    print("What item would you like to use?")

def potion():
    if player.hp == player.max_hp:
        print("Your health is already full!")
        return
    elif player.max_hp - player.hp <= 5:
        player.hp = player.max_hp
    else:
        player.hp += 5

def escape_powder():
    pass

def molotov():
    pass



main()