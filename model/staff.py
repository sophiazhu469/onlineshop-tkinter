from model.user import User
from datetime import date

# The Staff Class
class Staff(User):
    allCustomerOrders=[]
    nextID = 100
    def __init__(self, sName: str, sPassword: str):
        self.__userRole='staff'
        self.__staffPassword = sPassword
        self.__staffName=sName
        self.__staffID = Staff.nextID
        Staff.nextID += 1

    
    @property
    def userRole(self):
        return self.__userRole
        
    @property
    def staffID(self):
        return self.__staffID

    @property
    def staffPassword(self):
        return self.__staffPassword 

    @property
    def staffName(self):
        return self.__staffName    


    @staffPassword.setter
    def staffPassword(self,value):
        self.__staffPassword=value

    
    def __eq__(self,other):
        return (self.staffName,self.staffPassword)==(other.staffName,other.staffPassword)
       

    def staffAddOrder(self,aOrder):
        self.allCustomerOrders.append(aOrder)
    


    def staffViewOrders(self):
        for order in self.allCustomerOrders:
            return order

    def updateOrderStatus(self,orderID: int ,value):
        for order in self.allCustomerOrders:
            if orderID==order.orderID:
                order.orderStautus=value

        
    
    def generateOrderReport(self,startDate: date, endDate:date ):
        for order in self.allCustomerOrders:
            if order.dateCreated>= startDate and order.dateCreated<= endDate:
                return order

    def staffLogIn(self,staffName: str, sPassword: str) -> str :
        if self.staffName==staffName and self.staffPassword==sPassword:
            return True
        else:
            return False

 


# staff1 = Staff('sophia','dddddd')
# staff2 = Staff('Rene','12345')
# print(staff1.staffID)
# print(staff1.staffName)    
# print(staff2.staffID)
# print(staff2.staffName)