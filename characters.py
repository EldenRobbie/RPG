# Need to add a defense stat based on using defend() that combines defense stat with armor defense

class Character:
    def __init__(self, name, max_hp, health, attack, base_defense, defense, agility, items):
        self.name = name
        self.max_hp = max_hp
        self.health = health
        self.attack = attack
        self.base_defense = base_defense
        self.defense = defense
        self.agility = agility
        self.items = []


char1 = Character(
name="Robbie", 
max_hp=5, 
health=5,
attack=2,
base_defense=0,
defense=1,
agility=3,
items=[]
)

