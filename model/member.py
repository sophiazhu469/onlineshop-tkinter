from datetime import date
from model.customer import Customer
# from model.order import Order
from model.shoppingCart import ShoppingCart
from model.payment import Payment,CCPayment,BankPayment


class Member(Customer):
    """! The Member Class"""
    nextID = 300
    def __init__(self,mName: str, mCart , mPhone: str, mEmail: str,mPassword: str):
        """! The initialiser for Member"""
        self.__userRole='member'
        self.__memberID = Member.nextID
        self.__memberName=mName
        self.__memberPhone = mPhone
        self.__memberEmail = mEmail
        self.__memberPassword = mPassword
        self.__allMyOrders = []
        self.__myShoppingCart=mCart
        Member.nextID += 1

    @property
    def userRole(self):
        return self.__userRole

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

    @property      
    def memberEmail(self):
        return self.__memberEmail

    @property
    def memberPassword(self):
        return self.__memberPassword


    @property
    def allMyOrders(self):
        return self.__allMyOrders  



    @myShoppingCart.setter
    def myShoppingCart(self,value):
        self.__myShoppingCart=value


    @memberPhone.setter
    def memberPhone(self,value):
        self.__memberPhone=value

    @memberEmail.setter
    def memberEmail(self,value):
        self.__memberEmail=value


    @memberPassword.setter
    def memberPassword(self,value):
        self.__memberPassword=value  




    def __eq__(self,other) -> bool:
        # To compare 2 member objects if they are the same one by email
        return (self.memberEmail==other.memberEmail)

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
        for order in self.allMyOrders:
            return order
             

    
    def addOrder(self,aOrder) :
        # Add order to member's order list
        self.allMyOrders.append(aOrder)

    def cancelOrder(self,aOrder) :
        aOrder.orderStatus='Cancelled'


    def trackMyOrderStatus(self,aOrder) -> str:
        # Member select an order and check its status ??????????????????
        if aOrder in self.allMyOrders:
            return aOrder.orderstatus
            
       

    def checkOut(self) -> None:
        # Clear Shopping Cart after an instance of Order Class created
        # aOrder=Order(date.today(),self)
        self.addOrder()
        self.myShoppingCart=[]

    def makePayment(self,amount):
        # member make payment for the new created Order object
        aPayment=Payment(amount)
        

    def addDeliveryAddress(self,address):
        self.order.deliveryAddress=address
