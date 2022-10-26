
class Category:
    nextID=400
    def __init__(self,categoryName: str):
        self.__categoryID=Category.nextID
        self.__categoryName=categoryName
        self.__productList=[]
        Category.nextID += 1

    def __eq__(self,other):
        return self.categoryName==other.categoryName

    def __str__(self):
        return str(self.__categoryID) + self.__categoryName   

    @property
    def categoryName(self):
        return self.__categoryName

    @property 
    def categoryID(self):
        return self.__categoryID
    
    @property
    def productList(self):
        return self.__productList

    @categoryName.setter
    def categoryName(self,value):
        self.categoryName=value      

    def getProductList(self):
        productList=[]
        for product in self.__productList:
            productList.append(product)
        return productList    
              
    def countProducts(self):
        return len(self.productList)

    def addProduct(self,aProduct):
        self.productList.append(aProduct)    