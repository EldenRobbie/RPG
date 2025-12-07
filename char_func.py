from clr_screen import *
from characters import *

def level_up():
    if player.xp_to_next_lvl <= 0:
        player.level += 1
        print(f"{player.name} leveled up to {player.level}!")
        
    