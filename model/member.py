from datetime import date
from model.badRequestError import BadRequestError
from model.customer import Customer
# # from model.order import Order
from model.shoppingCart import ShoppingCart
from model.payment import Payment,CCPayment,BankPayment


class Member(Customer):
    """! The Member Class"""
    nextID = 300
    def __init__(self,mName: str, mCart,mPhone: str, mEmail: str,mPassword: str):
        """! The initialiser for Member"""
        self.__memberID = Member.nextID
        self.__memberName=mName
        self.__memberPhone = mPhone
        self.__memberEmail = mEmail
        self.__memberPassword = mPassword
        self.__allMyOrders = []
        self.__myShoppingCart=mCart
        Member.nextID += 1



    @property
    def myShoppingCart(self):
        return self.__myShoppingCart

    @property
    def memberName(self):
        return self.__memberName  

    
    @property
    def memberID(self):
        return self.__memberID

    @property
    def memberPhone(self):
        return self.__memberPhone

    @memberPhone.setter
    def memberPhone(self,value):
        self.__memberPhone=value    

    @property      
    def memberEmail(self):
        return self.__memberEmail

    @memberEmail.setter
    def memberEmail(self,value):
        self.__memberEmail=value
    

    @property
    def memberPassword(self):
        return self.__memberPassword

    @memberPassword.setter
    def memberPassword(self,value):
        self.__memberPassword=value      


    @property
    def allMyOrders(self):
        return self.__allMyOrders  



    @myShoppingCart.setter
    def myShoppingCart(self,value):
        self.__myShoppingCart=value



    def __eq__(self,other) -> bool:
        # To compare 2 member objects if they are the same one by email
        return (self.memberName==other.memberName and self.memberPassword==other.memberPassword)

    def __str__(self):
        return self.memberName + ' ' + self.memberPhone + ' ' + self.memberEmail    

    def memberLogIn(self,memberName: str, memberPassword: str):
        # Member use name and password to log in
        if self.memberName==memberName and self.memberPassword==memberPassword:
            return True
        else:
            return False
          

    def viewAllMyOrders(self):
        # Display all Orders for this Member
        myOrderList=[]
        for order in self.allMyOrders:
            myOrderList.append((order.orderID,order.dateCreated,order.orderStatus,order.calOrderTotalAmount()))
        return myOrderList
             
    def searchOrder(self,orderID):
        for order in self.allMyOrders:
            if order.orderID==orderID:
                return order
    
    def addOrder(self,aOrder) :
        # Add order to member's order list
        self.allMyOrders.append(aOrder)

    def cancelOrder(self,aOrder):
        if aOrder.orderStatus in ['processing', 'awaiting shipment']:
            aOrder.orderStatus='cancelled'
            return True
        else:
            return False
            # raise BadRequestError('This order cannot be cancelled')    


    def trackMyOrderStatus(self,aOrder) -> str:
        # Member select an order and check its status ??????????????????
        if aOrder in self.allMyOrders:
            return aOrder.orderStatus
            
       

    def makePayment(self,amount):
        # member make payment for the new created Order object
        aPayment=Payment(amount)
        return True
        

