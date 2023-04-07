import csv

with open('./data/currencyrates.csv','r') as file:
    lines=csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(f'50$ usd to bangla taka:{50*float(line[3])} taka')