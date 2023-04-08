class Aircraft:
    def __init__(self,make,code,tpe,flight_range) -> None:
        self.make=make
        self.code=code
        self.tpe=tpe
        self.flight_range=flight_range
    def get(self):
        return self.make
    def __repr__(self) -> str:
        return f'make:{self.make} code: {self.code} tpe:{self.tpe} flight_range:{self.flight_range}'
