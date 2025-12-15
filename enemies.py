class Enemy:
    def __init__(self, name, hp, attack, defense, accuracy, xp_grant, item_grant):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.xp_grant = xp_grant
        self.item_grant = item_grant

enemy_1 = Enemy("slime", 3, 1, 0, 1, 5, [])

enemy_2 = Enemy("bat", 5, 1, 1, 1, 7, [])

enemy_3 = Enemy("rat", 8, 2, 1, 1, 10, [])

enemy_4 = Enemy("wolf", 12, 3, 2, 3, 15, [])

random_enemy = False
enemy_list = [enemy_1, enemy_2, enemy_3, enemy_4]
if random_enemy == False:
    enemy = enemy_1
elif random_enemy == True:
    enemy = random.choice(enemy_list)


'''
How am I going to do this?
1. Add all the enemies to a list.
2. Randomly choose an enemy from the list to fight.
    - Use a different function to call a random enemy, that way testing is easier.
'''