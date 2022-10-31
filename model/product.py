from model.category import Category

class Product:
    """! The Product Class"""
    nextID=500
    def __init__(self,pName: str,  pCategory: Category, pDescr: str, pPrice: float):
        """! The initializer for Product"""
        self.__productID = Product.nextID
        self.__productName = pName
        self.__productCategory = pCategory
        self.__productDescrip = pDescr
        self.__productPrice = pPrice
        pCategory.addProduct(self)
        Product.nextID += 1
    
    @property
    def productID(self):
        return self.__productID

    @property
    def productName(self):
        return self.__productName

    @property
    def productCategory(self):
        return self.__productCategory

    @property
    def productPrice(self):
        return self.__productPrice

    @property
    def productDescrip(self):
        return self.__productDescrip



    @productName.setter
    def productName(self,value):
        self.__productName=value

    @productCategory.setter
    def productCategory(self,value):
        self.__productCategory=value

    @productPrice.setter
    def productPrice(self,value):
        self.__productPrice=value

    @productDescrip.setter
    def productDescrip(self,value):
        self.__productDescrip= value
             


    def __str__(self) -> str:
        # Dunder method to return details of the product
        return 'Product ID:' + str(self.__productID) + '\nProduct Name: '+ self.__productName + '\nProduct Category: '+ self.__productCategory.categoryName + '\nDescription: '+ self.__productDescrip + '\nPrice: $'+ self.__productPrice +'\n\n'

    def __eq__(self,other) -> bool:
        # Compare product name with a given product name to check if it is the same product
        return self.productName==other.productName


    # def __eq__(self,other) -> bool:
    #     # Compare product Category with a given Category
    #     return self.productCategory==other.productCategory


    def displayProduct(self):
        return self.productName + ':$' + str(self.productPrice)
      