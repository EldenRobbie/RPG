import random
from characters import *
from enemies import *
from clr_screen import *
# print(random.randint(1,6))

def main():
    battle()


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
            print("You use an item.")
            return
        
        elif pmt == "4" or pmt == "flee":
            clear_screen()
            print("You flee.")
            return
        
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
        return 
    else:
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
    pass


def flee():
    pass


main()
