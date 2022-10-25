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
       return self.myShoppingCart.addItem(aProduct)


    def removeItem(self,anItem):
        self.myShoppingCart.removeItem(anItem)
   
        
    def viewCartDetails(self)-> str:
        return self.myShoppingCart.viewCartDetails()

    def emptyCart(self):
        self.myShoppingCart.emptyCart()    

    def checkOut(self) -> None:
        self.myShoppingCart=[]    



