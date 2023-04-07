class Airport:
    def __init__(self,code,name,city,country,lat,long,rate) -> None:
        self.code=code
        self.name=name
        self.city=city
        self.country=country
        self.lat=lat
        self.long=long
        self.rate=rate

    def __repr__(self) -> str:
        return f'airport-name:{self.name} country:{self.country} latitude:{self.lat} longitude:{self.long} rate:{self.rate}'