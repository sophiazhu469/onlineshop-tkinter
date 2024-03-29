from model.user import User
from model.shoppingCart import ShoppingCart


class Customer(User):
    def __init__(self,aCart:ShoppingCart,cName: str):
        self._myShoppingCart = aCart
        super().__init__(cName)

    @property
    def myShoppingCart(self):
        return self._myShoppingCart    

    @myShoppingCart.setter
    def myShoppingCart(self,value):
        self._myShoppingCart=value    

    def addItem(self,aProduct):
        self.myShoppingCart.addItem(aProduct)


    def removeItem(self,anItem):
        self.myShoppingCart.removeItem(anItem)
   
        
    def viewCartDetails(self)-> str:
        return self.myShoppingCart.viewCartDetails()

    def emptyCart(self):
        self.myShoppingCart.emptyCart()    





