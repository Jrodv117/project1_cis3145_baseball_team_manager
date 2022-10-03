import csv


def open_read_csv():
    try:
        with open("BaseballPlayers.csv", mode='r', encoding='utf-8-sig') as data_file:
            DATA = csv.reader(data_file)
            player_stats = []
            for row in DATA:
                player_stats.append([row[0], row[1], row[2], row[3]])
            return player_stats
    except:
        print("ERROR CSV FILE NOT FOUND OR COULDN'T BE READ")
        exit()


def save_to_csv(player_information):
    with open("BaseballPlayers.csv", 'w') as data_file:
        writer = csv.writer(data_file)
        for row in player_information:
            try:
                writer.writerow([row[0], int(row[1]), int(row[2]),int(row[3])])
            except:
                writer.writerow([row[0], row[1],row[2], row[3]])
