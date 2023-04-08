import csv

with open('./data/friends.csv','r') as file:
    lines=csv.reader(file)
    # to skip head in csv file
    header=next(lines)
    for line in lines:
        print(line)