class Enemy:
    def __init__(self, name, health, attack, defense, items):
        self.name = name
        self.health = health
        self.attack = attack
        self. defense = defense
        self.items = []

enemy1 = Enemy(
    name="slime",
    health=3, 
    attack=1, 
    defense=0, 
    items=[]
    )
