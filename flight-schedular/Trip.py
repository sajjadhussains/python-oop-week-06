class Trip:
    def __init__(self,trip_cities,aircraft,price,start_date,route='') -> None:
        self.tripe_cities=trip_cities
        self.start_date=start_date
        self.aircraft=aircraft
        self.trip_route=route
        self.price=price

    def __repr__(self) -> str:
        return f'Trip:{self.tripe_cities} Start date:{self.start_date} Aircraft:{self.aircraft} Route:{self.trip_route} Cost:{self.price} '
       