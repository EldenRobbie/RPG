# stats: Name, Level, Current XP Max HP, Current HP, Attack, Defense, Accuracy

# Attack, Defend, Item, Flee

class Character:
    def __init__(self, name, level, xp, max_hp, hp, attack, defense, accuracy, agility, items):
        self.name = name
        self.level = level
        self.xp = xp
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.agility = agility
        self.items = items
        self.xp_to_next_lvl = level * 5

player = Character("Robbie", 1, 0, 5, 5, 2, 0, 1, 3, [])

