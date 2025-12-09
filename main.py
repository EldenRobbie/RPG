from battle import *
from characters import Character, player
from clr_screen import *

def main():
    # check status, battle, use item, talk
    story()
    clear_screen()
    battle()
    input("Let's go again to test out your new stats!")
    battle()
    

def story():
    nam = input("What's your name? ")
    player.name = nam


main()