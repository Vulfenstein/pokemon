import csv

File = open("pokemonNames.txt", "w")

with open('pokemon.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        File.write(str(row[1]).lower())
        File.write('\n')
File.close