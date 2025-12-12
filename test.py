import random
from characters import *
from enemies import *
from clr_screen import *

'''
Pick an enemy from the list, then use that as a variable.

'''

enemy_list = [enemy_1, enemy_2, enemy_3, enemy_4]

# print(random.choice(enemy_list).name)



def testing():
    enemy = random.choice(enemy_list)
    print(enemy.name)
    print(enemy.hp)
    print(enemy.attack)

testing()