from extra import clear_screen

def main():
    m_c = introduction()
    


def introduction():
    print("Welcome to the world!")
    nam = input("What's your name? ")
    if nam.isdigit():
        print("That's not a name!")
    else:
        print(f"Welcome to the world, {nam}!")
    return nam


main()