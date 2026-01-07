import os
from enemies import *
from characters import *

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def player_hp_check():
    if char1.health <= 0:
        input(f"Oh no! {char1.name} died!")
        clear_screen()
        
        input("GAME OVER")
        clear_screen()
        
        return True


def enemy_hp_check():
    if enemy1.health <= 0:
        print(f"The {enemy1.name} died!")
        
        return True