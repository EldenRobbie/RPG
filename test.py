from characters import *
from enemies import *
from clr_screen import *

'''
Need to add xp to xp_need_to_next_lvl

'''


char = player.name
lvl = player.level
nxt = player.xp_to_next_lvl

# print(f"{char}'s level is: {lvl}.")
# print(f"XP to next level: {player.xp_to_next_lvl}")
# input("")
# clear_screen()

# player.xp += 5
# print(f"{char} gained 5 xp!")
# input(f"Total XP = {player.xp}")
# clear_screen()

# if player.xp >= player.xp_to_next_lvl:
#     player.level += 1
#     player.xp_to_next_lvl = player.level * 5
#     print(f"{char} leveled up!")
#     input("")
#     clear_screen()
# else:
#     pass

# print(f"Level: {player.level}")
# print(f"XP to next level: {player.xp_to_next_lvl}")
# print("")


# print("Victory!")
# print("Doot doo doo doo, doo doo, doot doo doo!")
# input("")
# clear_screen()

# print(f"{char}'s XP is: {player.xp}")
# print(f"{char} gained {enemy_1.xp_grant} XP!")
# input("")
# clear_screen()

# player.xp += enemy_1.xp_grant

# print(f"{char}'s XP is: {player.xp}")

print(f"XP to gain: {player.xp_to_next_lvl}")
print(f"Gained {enemy_1.xp_grant} XP!")
player.xp_to_next_lvl = player.xp_to_next_lvl - enemy_1.xp_grant

input("")
clear_screen()

print(f"XP to gain: {player.xp_to_next_lvl}")