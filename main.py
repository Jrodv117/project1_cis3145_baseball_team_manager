def menu():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\tBaseball Team Management Program")
    print("MENU OPTIONS")
    print(
        "1 - Display lineup\n"
        + "2 - Add player\n"
        + "3 - Remove player\n"
        + "4 - Move player\n"
        + "5 - Edit player position\n"
        + "6 - Edit player stats \n"
        + "7 - Exit program\n"
    )
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


def display_lineup():
    print("lineup")


def add_player():
    print("add player")


def main():
    menu()
    while True:
        user_selection = int(input("Menu option: "))
        if user_selection == 1:
            display_lineup()
        elif user_selection == 2:
            add_player()


main()
