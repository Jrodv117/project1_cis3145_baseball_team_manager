from click import edit


def menu():
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


def display_lineup():
    print("lineup")


def add_player():
    print("add player")


def remove_player():
    print("remove player")


def move_player():
    print("move player")


def edit_player_position():
    print("edit player position")


def edit_player_stats():
    print("edit player stats")


def main():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\tBaseball Team Management Program")
    menu()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    player_information = [
        ["Trevor", "SS", "588", "173"],
        ["Garrett", "2B", "299", "74"],
        ["Tony", "C", "535", "176"],
        ["Hunter", "RF", "580", "182"],
        ["Ian", "CF", "443", "113"],
        ["Nolan", "3B", "588", "185"],
        ["Daniel", "1B", "438", "122"],
        ["David", "LF", "374", "113"],
        ["Phillip", "P", "102", "12"],
    ]

    while True:
        user_selection = int(input("Menu option: "))
        if user_selection == 1:
            display_lineup()
        elif user_selection == 2:
            add_player()
        elif user_selection == 3:
            remove_player()
        elif user_selection == 4:
            move_player()
        elif user_selection == 5:
            edit_player_position()
        elif user_selection == 6:
            edit_player_stats()
        elif user_selection == 7:
            exit()
        else:
            print("Invalid Menu Selection\n")
            menu()


main()
