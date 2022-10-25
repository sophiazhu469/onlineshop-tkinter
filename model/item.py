from model.product import Product


class Item:
    """! The Item Class"""
    def __init__(self,aProduct: Product, quantity: int=1):
        """! The initialiser for Order"""
        
        self.__itemProduct=aProduct
        self.__quantity=quantity
        self.__itemID=aProduct.productID


    # def __str__(self):
    #     return (self.__itemProduct.productName,str(self.__quantity) ,str(self.calculateTotal()))  

    def __eq__(self,other):
        return self.itemProduct.productName==other.itemProduct.productName   

    @property
    def itemProduct(self):
        return self.__itemProduct


    @property
    def itemID(self):
        return self.__itemID    

        

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,value):
        self.__quantity=value


    def calculateTotal(self):
        return float(self.itemProduct.productPrice)*self.quantity     