import csv
from Airport import Airport

class allAirports:
    def __init__(self) -> None:
        self.load_airport_data('./data/airport.csv')
    def load_airport_data(self,fileName):
        airports={}
        currency_rates={}
        country_currency={}

        # get currency name<----->rate
        with open('./data/currencyrates.csv','r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]]=line[2]
        file.close()

        # dictionary country<--->currency
        with open('./data/countrycurrency.csv','r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]]=line[1]
        file.close()

        with open(fileName,'r',encoding="utf8") as file:
            lines=csv.reader(file)
            try:
                for line in lines:
                    country=line[3]
                    currency=country_currency[country]
                    rate=currency_rates[currency]
                    airports[line[4]]=Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
            except KeyError as e:
                print(e)
            self.airports=airports
            for airport in airports.items():
                print(airport)

allAirports()