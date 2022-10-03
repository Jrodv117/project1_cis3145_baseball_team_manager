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


def add_player(player_information, valid_positions):
    new_player = []
    new_player.append(input("Enter Player Name: "))
    position = input("Enter Player Position: ")
    while position not in valid_positions:
        position = input("Enter a valid position: ")
    new_player.append(position)
    new_player.append(input("Enter At Bats: "))
    new_player.append(input("Enter hits: "))
    player_information.append(new_player)
    print(player_information)
    print(f"{new_player[0]} was added")


def remove_player(player_information):
    lineup_number = int(input("Enter a line up number to remove: "))
    player = player_information[lineup_number - 1]
    player_information.pop(lineup_number - 1)
    print(player_information)
    print(f"{player[0]} was removed")


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

    valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    while True:
        user_selection = int(input("Menu option: "))
        if user_selection == 1:
            display_lineup()
        elif user_selection == 2:
            add_player(player_information, valid_positions)
        elif user_selection == 3:
            remove_player(player_information)
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
