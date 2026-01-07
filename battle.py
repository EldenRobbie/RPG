import random
from enemies import *
from characters import *
from extra import clear_screen, player_hp_check, enemy_hp_check
from items import *


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
            clear_screen()
            if player_hp_check == True:
                break

        elif option == "3" or option == "item":
            if item() == True:
                break

        elif option == "4" or option == "flee":
            if flee() == True:
                break

        else:
            print("Well that doesn't work!")

def attack():
    damage_done = char1.attack - enemy1.defense
    
    print(f"{char1.name} attacked {enemy1.name} for {damage_done} damage!")
    enemy1.health -= damage_done
    
    if enemy1.health > 0:
        input(f"{enemy1.name} has {enemy1.health} hp!   ")

   

def defend():
    defended_damage = enemy1.attack - char1.defense
    
    input(f"{char1.name} defended!")
    clear_screen()

    input(f"{enemy1.name} attacked {char1.name} for {defended_damage} damage!")
    clear_screen()

    char1.health -= defended_damage

    if char1.health > 0:
        input(f"{char1.name} has {char1.health} hp!   ")


def item():
    print("What item would you like to use?")
    print("(1) Potion")
    print("(2) Escape Powder")
    print("(3) Molotov")
    choice = input("").lower()
    clear_screen()
    if choice == "1" or choice == "potion":
        potion()

    elif choice == "2" or choice == "escape powder":
        if escape_powder() == True:
            return True

    elif choice == "3" or choice == "molotov":
        if molotov() == True:
            return True


def flee():
    num = random.randint(1, 20) + char1.agility
    if num >= 10:
        input(f"{char1.name} successfully escaped!")
        clear_screen()
        return True
    
    else:
        input(f"{char1.name} was unable to escape...")
        clear_screen()

def enemy_retaliate():
    damage_done = enemy1.attack - char1.base_defense
    
    input(f"{enemy1.name} attacked {char1.name} for {damage_done} damage!")
    clear_screen()
    
    char1.health -= damage_done
    
    if char1.health > 0:
        input(f"{char1.name} has {char1.health} hp!")
        clear_screen()





main()