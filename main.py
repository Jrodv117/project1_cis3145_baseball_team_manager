# Julian Rodriguez-Vera
# Team Manager
# 10/02/2022
# This programn creates a simple program that allows user to manage his/her baseball team.

import FileIO


def title():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\tBaseball Team Management Program")
    menu()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


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


def display_lineup(player_information):
    print("   Player " + "POS" + " AB " + "  H" + "    AVG ")
    print("----------------------------------------------------------")
    i = 0
    for index in player_information:
        if len(index) == 4:
            print(i + 1, end=" ")
        for m in index:
            print(m + " ", end=" ")
        try:
            print(round(float(index[3]) / float(index[2]), 3), end=" ")
        except:
            print("0.00", end=" ")
        i = i + 1
        print("")
    print("\n")


def add_player(player_information, valid_positions):
    new_player = []
    new_player.append(input("Enter Player Name: "))
    position = input("Enter Player Position: ")
    while position not in valid_positions:
        position = input("Enter a valid position: ")
    new_player.append(position)
    new_player.append(input("Enter At bats: "))
    new_player.append(input("Enter Hits: "))
    player_information.append(new_player)
    print(f"{new_player[0]} was added\n")
    FileIO.save_to_csv(player_information)


def remove_player(player_information):
    lineup_number = int(input("Enter a line up number to remove: "))
    player = player_information[lineup_number - 1]
    player_information.pop(lineup_number - 1)
    print(f"{player[0]} was deleted.\n")
    FileIO.save_to_csv(player_information)


def move_player(player_information):
    current_index = int(input("Enter a current lineup number to move: "))
    current_player_at_index = player_information[current_index - 1]
    player_information.pop(current_index - 1)
    print(f"{current_player_at_index[0]} was selected.")
    player_information.insert(
        int(input("Enter a new lineup number: ")) - 1, current_player_at_index
    )
    print(f"{current_player_at_index[0]} was moved. \n")
    FileIO.save_to_csv(player_information)


def edit_player_position(player_information, valid_positions):
    lineup_number = int(input("Enter a lineup number to edit: "))
    player_at_index = player_information[lineup_number - 1]
    print(f"You selected {player_at_index[0]} POS={player_at_index[1]}")
    position = input("Enter a new position: ")
    while position not in valid_positions:
        position = input("Enter a valid position: ")
    player_at_index.pop(1)
    player_at_index.insert(1, position)
    print(f"{player_at_index[0]} was updated.\n")
    FileIO.save_to_csv(player_information)


def edit_player_stats(player_information):
    lineup_number = int(input("Enter a lineup number to edit"))
    player_at_index = player_information[lineup_number - 1]
    print(
        f"You selected {player_at_index[0]} AB: {player_at_index[2]} H: {player_at_index[3]}"
    )
    while True:
        try:
            edit = input(f"Edit AB for {player_at_index[0]}?(y/n): ").lower()
            if edit == "y":
                player_at_index.pop(2)
                at_bats = int(input("enter new AB: "))
                player_at_index.insert(2, at_bats)
            elif edit == "n":
                pass
        except (ValueError):
            print("invalid entry please enter a valid number")
        break
    while True:
        try:
            edit = input(f"Edit H for {player_at_index[0]}?(y/n): ").lower()
            if edit == "y":
                player_at_index.pop(3)
                hits = int(input("enter new H: "))
                player_at_index.insert(3, hits)
            elif edit == "n":
                pass
        except (ValueError):
            print("invalid entry please enter a valid number")
        break
    FileIO.save_to_csv(player_information)


def main():
    title()

    player_information = FileIO.open_read_csv()

    valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    while True:
        try:
            user_selection = int(input("Menu option: "))
            if user_selection == 1:
                display_lineup(player_information)
            elif user_selection == 2:
                add_player(player_information, valid_positions)
            elif user_selection == 3:
                remove_player(player_information)
            elif user_selection == 4:
                move_player(player_information)
            elif user_selection == 5:
                edit_player_position(player_information, valid_positions)
            elif user_selection == 6:
                edit_player_stats(player_information)
            elif user_selection == 7:
                print("Bye!")
                exit()
            else:
                print("Please input a valid menu selection\n")
                menu()
        except (ValueError, TypeError):
            print("Please input a valid menu selection\n")
            menu()


main()
