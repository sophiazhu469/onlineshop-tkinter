from model.member import Member
from model.customer import Customer
from model.shoppingCart import ShoppingCart

class Guest(Customer):
    """! The Guest Class"""
    nextID = 200
    def __init__(self,aCart):
        """! The initialiser for Guest"""
        self._myShoppingCart=aCart
        # super().__init__(aCart)
        self.__guestName='guest'
    

    @property
    def guestName(self):
        return self.__guestName

    @property
    def myShoppingCart(self):
        return self._myShoppingCart   

    def register(self,mName,mPhone,mEmail,mPassword):
        aMember=Member(mName,mPhone,mEmail,mPassword)
        return aMember

aCart=ShoppingCart()
aGuest=Guest(aCart)
print(aGuest.guestName)
