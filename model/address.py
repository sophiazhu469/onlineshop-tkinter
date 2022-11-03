class Address:
    # The Address Class
    def __init__(self,street:str, suburb: str, city: str,postcode: str):
        self.__myStreet = street
        self.__mySuburb = suburb
        self.__myCity = city
        self.__myPostcode =postcode

    def __str__(self):
        return self.__myStreet+ ',' + self.__mySuburb +','+ self.myCity + ' '+ self.__myPostcode  


    @property
    def myStreet(self):
        return self.__myStreet

    @property
    def mySuburd(self):
        return self.__mySuburb

    @property
    def myCity(self):
        return self.__myCity


    @property
    def myPostcode(self):
        return self.__myPostcode    



    @myStreet.setter
    def myStreet(self,value):
        self.__myStreet=value


    @mySuburd.setter
    def mySuburd(self,value):
        self.__mySuburb=value

    @myCity.setter
    def myCity(self,value):
        self.__myCity=value     

    @myPostcode.setter
    def myPostcode(self,value):
        self.__myPostcode=value   