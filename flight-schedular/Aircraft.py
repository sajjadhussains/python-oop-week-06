class Aircraft:
    def __init__(self,make,code,tpe,flight_range) -> None:
        self.make=make
        self.code=code
        self.tpe=tpe
        self.flight_range=flight_range

    def get_make(self):
        return self.make
    
    def __repr__(self) -> str:
        return f'making-company: {self.make} code:{self.code} type:{self.tpe} flight-range:{self.flight_range}'
    
    