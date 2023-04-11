import csv
from Aircraft import Aircraft

class Air_lines:
    def __init__(self) -> None:
        self.aircrafts=None
        self.load_aircrafts_data('./data/aircraft.csv')

    def load_aircrafts_data(self,file):
        aircrafts={}
        with open(file,'r') as file:
            lines=csv.reader(file)
            next(lines)
            for line in lines:
                aircrafts[line[0]]=Aircraft(line[3],line[0],line[1],line[4])
        file.close()
        self.aircrafts=aircrafts
        # for air in aircrafts.items():
        #     print(air)
    def get_aircraft(self,aircraft_code):
        return self.aircrafts[aircraft_code]
    def get_aircraft_by_distance(self,distance):
        for aircraft in self.aircrafts.values():
            if aircraft.flight_range<distance:
                return aircraft


Air_lines()