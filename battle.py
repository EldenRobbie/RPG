import random
import sys
from characters import *
from enemies import *
from clr_screen import *
from char_func import *

random_enemy = True
enemy_list = [enemy_1, enemy_2, enemy_3, enemy_4]
if random_enemy == False:
    enemy = enemy_1
elif random_enemy == True:
    enemy = random.choice(enemy_list)

def battle():
    print(f"A wild {enemy.name} appears!")
    input("")
    clear_screen()
    print(f"{player.name} has {player.hp} HP.")
    while True:   
        input("")
        clear_screen()
        print("What would you like to do?")
        print("1. Attack 2. Defend 3. Item 4. Flee ")
        prompt = input("")
        pmt = prompt.lower()
        
        if pmt == "1" or pmt == "attack":
            attack()
            if enemy.hp > 0:
                continue
            else:
                break
            
        elif pmt == "2" or pmt == "defend":
            defend()
            if player.hp > 0:
                continue
            else:
                break


        elif pmt == "3" or pmt == "item":
            item()
        
        elif pmt == "4" or pmt == "flee":
            clear_screen()
            if player.hp <= 0:
                print("GAME OVER")
                return
            else:
                flee_result = flee()
                if flee_result == 1:
                    break
                else:
                    continue

     
        else:
            print("That's an invalid input.")
            

def attack():
    clear_screen()
    print(f"{enemy.name}'s health is {enemy.hp}.")
    print(f"{player.name} attacks the {enemy.name} for {player.attack} damage.")
    enemy.hp -= player.attack
    
    if enemy.hp <= 0:
        clear_screen()
        print("Victory!")
        print("Doot doo doo doo, doo doo, doot doo doo!")
        input("")
        clear_screen()

        level_up()
        return 
    else:
        input("")
        clear_screen()
        print(f"{enemy.name} attacks {player.name} for {enemy.attack} damage.")
        player.hp -= enemy.attack
        input("")
        clear_screen()
        if player.hp <= 0:
            print("GAME OVER")
            sys.exit(1)
        else:
            print(f"{player.name}'s hp is: {player.hp}.")
            print(f"{enemy.name}'s hp is: {enemy.hp}.")
            


def defend():
    clear_screen()
    blocked_dmg = enemy.attack - player.defense
    print(f"{player.name}'s hp is: {player.hp}, they defend!")
    print(f"{enemy.name} attacks {player.name} for {blocked_dmg} damage.")
    player.hp -= blocked_dmg
    input("")
    clear_screen()
    if player.hp <= 0:
        print("GAME OVER")
        sys.exit(1) 
    else:
        print(f"{player.name}'s hp is: {player.hp}.")


def item():
    clear_screen()
    print("Items:")
    print(item_list)
    print("")
    ans = input("What item would you like to use? ")
    if ans.lower() == "potion":
        if item_list["potion"] > 0:
            potion()
        else:
            print("You don't have any potions!")
    elif ans.lower == "":
        pass


def flee():
    msg = ("You try to flee.")
    print(msg)
    input("")
    clear_screen()
    print(msg)
    input(".")
    clear_screen()
    print(msg)
    input(". .")
    clear_screen()
    print(msg)
    input(". . .")
    clear_screen()

    flee_roll = random.randint(1, 100) + (player.agility * 3)
    if flee_roll >= 75:
        print("Congratulations! You excaped!")
        return 1
    else:
        print("You were unable to escape!")
        input("")
        clear_screen()
        print(f"{player.name}'s hp is: {player.hp}.")
        print(f"{enemy.name} attacks {player.name} for {enemy.attack} damage.")
        player.hp -= enemy.attack
        input("")
        clear_screen()
        if player.hp <= 0:
            print("GAME OVER")
            sys.exit(1)
            
        else:
            print(f"{player.name}'s hp is: {player.hp}.")