from datetime import date
from model.member import Member
from model.address import Address
from model.payment import Payment

class Order:
    """! The Order Class"""
    nextID=600
    def __init__(self,dCreated: date,aMember:Member):
        """! The initialiser for Order"""
        self.__orderID = Order.nextID
        self.__dateCreated = dCreated
        self.__orderStatus = 'processing'
        self.__orderPayment = None
        self.__billingAddress = None
        self.__deliveryAddress = None
        self.__orderMember=aMember
        aMember.allMyOrders.append(self)
        self.__shippingNumber= None
        self.__allOrderItems=aMember.myShoppingCart.allItems #pass shopping cart's Itemlist to order
        aMember.myShoppingCart.allItems=[]  #after that clear shopping cart
        Order.nextID += 1


    @property
    def orderID(self):
        return self.__orderID

    @property
    def dateCreated(self):
        return self.__dateCreated

    @property
    def orderStatus(self):
        return self.__orderStatus

  
    @property
    def billingAddress(self):
        return self.__billingAddress

    @property
    def deliveryAddress(self):
        return self.__deliveryAddress

    @property
    def orderPayment(self):
        return self.__orderPayment


    @property
    def shippingNumber(self):
        return self.__shippingNumber

    @property
    def orderMember(self):
        return self.__orderMember    

    @property
    def allOrderItems(self):
        return self.__allOrderItems    

    @allOrderItems.setter
    def allOrderItems(self,value):
        self.__allOrderItems=value    

    @orderStatus.setter
    def orderStatus(self,newStatus: str):
        if newStatus not in ['processing', 'awaiting shipment', 'shipped', 'delivered','Cancelled']:
            raise ValueError('Order Status is not in range')
        self.__orderStatus = newStatus                    

    @orderPayment.setter
    def orderPayment(self, aPayment: Payment):
        self.__orderPayment = aPayment

    @billingAddress.setter
    def billingAddress(self,newBillAddress: Address):
        self.__billingAddress = newBillAddress

    @deliveryAddress.setter
    def deliveryAddress(self,newDelivAddress: Address):
        self.__deliveryAddress = newDelivAddress     

    @shippingNumber.setter
    def shippingNumber(self,newShipping: str):
        self.__shippingNumber = newShipping

    



    def __eq__(self,aOrder) -> bool:
        # Allow 2 order objects to be compared to check if they are the same object
        return self.orderID==aOrder.orderID  
    
    def calOrderTotalAmount(self)-> float:
        totalAmount=0
        # To calculate total amount for all the items in the Order plus delivery charge
        for item in self.allOrderItems:
            totalAmount += item.calculateTotal()
        # assume shipping cost is $5    
        return totalAmount + 5  
            
        

    def __str__(self) -> str:
        # To display order details
        return 'Order Number: '+ self.orderID + '\nOrder Date:' + self.dateCreated +'\nOrder Member: '+ \
        self.orderMember.memberName + '\nOrder Amount: $'+ self.orderPayment.amount + 'Order Status: ' + self.orderStatus