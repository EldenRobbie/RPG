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
        print(f"{player.name} leveled up to {player.level}!")
        
    