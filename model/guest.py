from model.member import Member
from model.customer import Customer

class Guest(Customer):
    """! The Guest Class"""
    nextID = 200
    def __init__(self,aCart,gName='guest'):
        """! The initialiser for Guest"""
        # self.__myShoppingCart=aCart
        self.__guestName=gName
        super().__init__(aCart)
    

    @property
    def guestName(self):
        return self.__guestName

    @property
    def myShoppingCart(self):
        return self._myShoppingCart   

    def register(self,mName,mPhone,mEmail,mPassword):
        aMember=Member(mName,mPhone,mEmail,mPassword)
        return aMember