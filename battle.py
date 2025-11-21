from extra import *
from characters import Character, player_1
from enemies import Enemy, enemy_1


def battle(combatant_1, combatant_2):
    # Give a choice to attack, defend or flee
    
    while True:
        choice = input("Would you like to attack, defend, or flee? ").lower()
        if choice == "attack":
            clear_screen()
            input(f"{player_1.name} is attacking: {enemy_1.name}!")
            clear_screen()
            
            return
        elif choice == "defend":
            clear_screen()
            print("You're defending!")
            return
        elif choice == "flee":
            clear_screen()
            print("You're fleeing!")
            return
        elif choice == "test":
            clear_screen()
            input(f"{player_1.name} is attacking: {enemy_1.name} for {player_1.attack} damage! ")
            clear_screen()
            input(f"{enemy_1.name}'s health before attack: {enemy_1.health}. ")
            enemy_1.health -= player_1.attack
            clear_screen()
            input(f"{enemy_1.name}'s health after attack: {enemy_1.health}. ")
            clear_screen()
            if player_1.health <= 0:
                print("Defeat!")
                return
            elif enemy_1.health <= 0:
                print("Victory!")
                return
            else:
                continue

        else:
            print("That's not a valid choice!")
        
battle(player_1, enemy_1)