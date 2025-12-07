class Enemy:
    def __init__(self, name, attack, defense, accuracy, xp_grant, item_grant):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.xp_grant = xp_grant
        self.item_grant = item_grant

enemy_1 = Enemy("slime", 1, 0, 1, 2, [])


