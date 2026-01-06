class Enemy:
    def __init__(self, name, health, attack, defense, items):
        self.name = name
        self.health = health
        self.attack = attack
        self. defense = defense
        self.items = []

enemy1 = Enemy("slime", 3, 1, 0, [])

print(enemy1.name)