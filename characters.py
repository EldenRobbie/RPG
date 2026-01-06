class Character:
    def __init__(self, name, max_hp, health, attack, defence, agility, items):
        self.name = name
        self.max_hp = max_hp
        self.health = health
        self.attack = attack
        self.defence = defence
        self.agility = agility
        self.items = []


char1 = Character("Robbie", 5, 5, 2, 1, 3, [])

