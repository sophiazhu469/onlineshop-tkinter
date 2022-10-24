from model.product import Product


class Item:
    """! The Item Class"""
    def __init__(self,aProduct: Product, quantity: int=1):
        """! The initialiser for Order"""
        self.__itemProduct=aProduct
        self.__quantity=quantity


    def __str__(self):
        return self.__itemproduct.productName +':' +self.__quantity   

    def __eq__(self,other):
        return self.itemProduct==other.itemProduct   

    @property
    def itemProduct(self):
        return self.__itemProduct

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,value):
        self.__quantity=value


    def calculateTotal(self):
        return self.itemProduct.productPrice*self.quantity     