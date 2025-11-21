class Enemy:
    def __init__(self, name, health, attack, defense, accuracy):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy

enemy_1 = Enemy("Slime", 5, 1, 0, 100)

