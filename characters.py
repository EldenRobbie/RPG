class Character:
    def __init__(self, name, max_hp, health, attack, defense, agility, items):
        self.name = name
        self.max_hp = max_hp
        self.health = health
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.items = []


char1 = Character("Robbie", 5, 5, 2, 0, 3, [])

