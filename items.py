from extra import *
from characters import *
from enemies import *
from extra import player_hp_check, enemy_hp_check

def potion():
#potion gives 5 HP
    input(f"{char1.name} has {char1.health} HP!")
    clear_screen()
    if char1.health == char1.max_hp:
        print(f"{char1.name}'s health is full!")

    elif char1.health < char1.max_hp:
        if (char1.health + 5) > char1.max_hp:
            char1.health = char1.max_hp
            input(f"{char1.name}'s health is now {char1.health}, it's full!")
            clear_screen()
        else:
            char1.health += 5
            input(f"{char1.name}'s health is now {char1.health}!")
            clear_screen()

def escape_powder():
    input(f"{char1.name} escaped!")
    return True


def molotov():
    input(f"{char1.name} used a molotov on {enemy1.name} for 5 damage!")
    clear_screen()
    enemy1.health -= 5
    if enemy_hp_check() == True:
        return True

