import random
from characters import *
from enemies import *
from clr_screen import *
from char_func import *

def battle():
    print(f"A wild {enemy_1.name} appears!")
    input("")
    clear_screen()
    print(f"{player.name} has {player.hp} HP.")
    while True:   
        input("")
        clear_screen()
        print("What would you like to do?")
        print("1. Attack, 2. Defend, 3. Item, 4. Flee ")
        prompt = input("")
        pmt = prompt.lower()
        
        if pmt == "1" or pmt == "attack":
            attack()
            if enemy_1.hp > 0:
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
            # print(f"flee equals: {flee()}")
            # if flee() == 1:
            #     break
            # elif flee() == 0:
            #     return
            # else:
            #     flee()
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
                break
            else:
                print("You were unable to escape!")
                input("")
                clear_screen()
                print(f"{player.name}'s hp is: {player.hp}.")
                print(f"{enemy_1.name} attacks {player.name} for {enemy_1.attack} damage.")
                player.hp -= enemy_1.attack
                input("")
                clear_screen()
                if player.hp <= 0:
                    print("GAME OVER")
                    break 
                else:
                    print(f"{player.name}'s hp is: {player.hp}.")

                continue

            
        else:
            print("That's an invalid input.")
            

def attack():
    clear_screen()
    print(f"{enemy_1.name}'s health is {enemy_1.hp}.")
    print(f"{player.name} attacks the {enemy_1.name} for {player.attack} damage.")
    enemy_1.hp -= player.attack
    
    if enemy_1.hp <= 0:
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
        print(f"{enemy_1.name} attacks {player.name} for {enemy_1.attack} damage.")
        player.hp -= enemy_1.attack
        input("")
        clear_screen()
        if player.hp <= 0:
            print("GAME OVER")
            return
        else:
            print(f"{player.name}'s hp is: {player.hp}.")
            print(f"{enemy_1.name}'s hp is: {enemy_1.hp}.")
            


def defend():
    clear_screen()
    blocked_dmg = enemy_1.attack - player.defense
    print(f"{player.name}'s hp is: {player.hp}, they defend!")
    print(f"{enemy_1.name} attacks {player.name} for {blocked_dmg} damage.")
    player.hp -= blocked_dmg
    input("")
    clear_screen()
    if player.hp <= 0:
        print("GAME OVER")
        return 
    else:
        print(f"{player.name}'s hp is: {player.hp}.")


def item():
    clear_screen()
    print("Sorry, there are no items to use right now.")


def flee():
    pass