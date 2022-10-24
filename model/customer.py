from model.user import User
from model.shoppingCart import ShoppingCart


class Customer(User):
    def __init__(self,cName: str,aCart:ShoppingCart):
        self._myShoppingCart = aCart
        super.__init__(cName)

    @property
    def myShoppingCart(self):
        return self._myShoppingCart    

    def addItem(self,aProduct):
       self.myShoppingCart.addItem(aProduct)


    def removeItem(self,anItem):
        self._myShoppingCart.remove(anItem)
   
        
    def viewCartDetails(self)-> str:
        return self._myShoppingCart.viewCartDetails()

    def checkOut(self) -> None:
        self._myShoppingCart=[]    



