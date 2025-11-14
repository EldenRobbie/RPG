from extra import clear_screen
from characters import characters

def main():
    # I need to fix the characters file to be able to access "stats."
    # I need to learn how to better use nested dictionaries and lists.
    characters["name"][0] = introduction()
    m_c = characters["name"][0]
    


def introduction():
    # This section is working as intended

    print("Welcome to the world!")
    nam = input("What's your name? ")
    clear_screen()
    if nam.isdigit():
        print("That's not a name!")
    else:
        print(f"Welcome to the world, {nam}!")
    return nam


main()