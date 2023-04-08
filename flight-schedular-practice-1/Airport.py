class Airport:
    def __init__(self,code,name,city,country_name,lat,long,rate) -> None:
        self.code=code
        self.name=name
        self.city=city
        self.country_name=country_name
        self.lat=lat
        self.long=long
        self.rate=rate
    
    def __repr__(self) -> str:
        return f'code:{self.code} name:{self.name} city:{self.city} country_name:{self.country_name} lat:{self.lat} long:{self.long} rate:{self.rate}'