# stats: Name, Level, Current XP Max HP, Current HP, Attack, Defense, Accuracy

# Attack, Defend, Item, Flee

class Character:
    def __init__(self, name, level, xp, xp_to_next_lvl, max_hp, hp, attack, defense, accuracy, items):
        self.name = name
        self.level = level
        self.xp = xp
        self.xp_to_next_lvl = xp_to_next_lvl
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.items = items

player = Character("Robbie", 1, 0, 10, 5, 5, 2, 0, 1, ["potato"])

