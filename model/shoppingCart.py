
from model.category import Category
from model.product import Product
from model.item import Item
from typing import List

class ShoppingCart:
    """! The Shopping Cart Class"""
    def __init__(self):
        """!The class initializer"""
        ## a list of instances of Orderline Class
        self.__allItems:List[Item] = []
       


    @property
    def allItems(self):
        return self.__allItems

    @allItems.setter
    def allItems(self,value):
        self.__allItems=value
        



    def addItem(self,aProduct:Product) -> None:
        # Add an Item Object and quantity of it to the shopping cart

        anItem=Item(aProduct,1)
        if len(self.__allItems)!=0:
            for item in self.__allItems:
                if item.itemProduct==anItem.itemProduct:
                    item.quantity= item.quantity+1
                    return True
            self.__allItems.append(anItem)  
        else:
            self.__allItems.append(anItem)
         
      
 

    def removeItem(self,anItem) -> None:
        # Remove an Item Object from the allItems list
        self.allItems.remove(anItem)

    def viewCartDetails(self)-> str:
        # To view all items in the shopping Cart
        itemList=[]
        for item in self.allItems:
            itemList.append((item.itemProduct.productName,item.quantity,item.calculateTotal()))
        return itemList

    def emptyCart(self):
        self.allItems=[]

    def getTotalSum(self) -> float: 
        totalSum=0
        # Use the Product Objects contained in the __allItems list to get Total Amount of the shopping cart
        for item in self.__allItems:
            totalSum += item.calculateTotal()
        return totalSum    


