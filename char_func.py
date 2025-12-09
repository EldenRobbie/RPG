import random
from clr_screen import *
from characters import *
from enemies import *


def level_up():
    player.xp += enemy_1.xp_grant
    player.xp_to_next_lvl = player.xp_to_next_lvl - enemy_1.xp_grant
    print(f"{player.name} gained {enemy_1.xp_grant} XP!")
    input("")
    clear_screen()

    if player.xp_to_next_lvl <= 0:
        player.level += 1
        player.xp_to_next_lvl = player.level * 5
        print(f"{player.name} leveled up to {player.level}!")
        input("")
        clear_screen()
        stats_up()


def stats_up():
    hp_up = random.randint(2, 5)
    
    att_up_chance = random.randint(1,5)
    att_up = 1

    def_up_chance = random.randint(1, 20)
    def_up = 0

    print(f"Player's max HP is: {player.max_hp}")
    player.max_hp += hp_up
    input("")
    clear_screen()
    print(f"Player's max HP is: {player.max_hp}")
    input("")
    clear_screen()

    print(f"Player Attack is: {player.attack}.")
    if att_up_chance == 5:
        att_up = 2
        player.attack += att_up
    else:
        att_up == 1
        player.attack += att_up
    input("")
    clear_screen()
    print(f"Player Attack is: {player.attack}.")
    input("")
    clear_screen()

    print(f"Player Defense is: {player.defense}.")
    if def_up_chance > 5:
        def_up = 1
        player.defense += def_up
    input("")
    clear_screen()
    print(f"Player Defense is: {player.defense}.")
    input("")
    clear_screen()

    



