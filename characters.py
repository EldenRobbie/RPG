# stats: Name, Max HP, Current HP, Attack, Defense, Accuracy

# Attack, Defend, Item, Flee

class Character:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

player = Character("Robbie", 3, 1)

