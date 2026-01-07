from enemies import *
from characters import *
from extra import clear_screen

def main():
    battle()

def battle():
    input(f"A {enemy1.name} appeared!")
    clear_screen()
    options()

def options():
    while True:
        print("What would you like to do")
        print("(1) Attack")
        print("(2) Defend")
        print("(3) Item")
        print("(4) Flee")
        option = input("").lower()
        clear_screen()
        
        if option == "1" or option == "attack":
            attack()
            clear_screen()
            if enemy_hp_check() == True:
                break
            enemy_retaliate()
            if player_hp_check() == True:
                break

        elif option == "2" or option == "defend":
            defend()

        elif option == "3" or option == "item":
            item()

        elif option == "4" or option == "flee":
            flee()

        else:
            print("Well that doesn't work!")

def attack():
    damage_done = char1.attack - enemy1.defense
    
    print(f"{char1.name} attacked {enemy1.name} for {damage_done} damage!")
    enemy1.health -= damage_done
    
    if enemy1.health > 0:
        input(f"{enemy1.name} has {enemy1.health} hp!   ")

   

def defend():
    print("You defended!")


def item():
    print("You used an item!")


def flee():
    print("You fled!")


def enemy_retaliate():
    damage_done = enemy1.attack - char1.defense
    
    input(f"{enemy1.name} attacked {char1.name} for {damage_done} damage!")
    clear_screen()
    
    char1.health -= damage_done
    
    if char1.health > 0:
        input(f"{char1.name} has {char1.health} hp!")
        clear_screen()


def player_hp_check():
    if char1.health <= 0:
        input(f"Oh no! {char1.name} died!")
        clear_screen()
        
        input("GAME OVER")
        clear_screen()
        
        return True


def enemy_hp_check():
    if enemy1.health <= 0:
        print(f"The {enemy1.name} died!")
        
        return True


main()