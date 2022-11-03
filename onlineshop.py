# Imports
from datetime import date, datetime
from logging import raiseExceptions


from model.category import Category
from model.address import Address
from model.customer import Customer
from model.guest import Guest
from model.item import Item
from model.member import Member
from model.order import Order
from model.payment import Payment,BankPayment,CCPayment
from model.product import Product
from model.shoppingCart import ShoppingCart
from model.staff import Staff
from model.user import User
from model.badRequestError import BadRequestError


from typing import List


class OnlineShop:
    # The OnlineShop class,Defines all the methods for the controller
    
    def __init__(self) :
        # The initialiser for OnlineShop
   
        self.allProducts: List[Product]= []
        self.allStaff: List[Staff] = []
        self.allMembers: List[Member] = []
        self.allCategories: List[Category] = []
        self.cart=ShoppingCart()
        self.guest=Guest('guest',self.cart)
        self.__initilizerCategory()
        self.__initilizerProduct()
        self.__initilizerUser()

    def createCategory(self,categoryName):
        #create an instance of category
        aCategory=Category(categoryName)
        if aCategory not in self.allCategories:   
            self.allCategories.append(aCategory)
            return aCategory    


        
    def __initilizerCategory(self):
        categoryFileName = open('category.txt','r')
        for line in categoryFileName:
            categoryName=line.rstrip().lower()
            self.createCategory(categoryName)  
        categoryFileName.close()

    def __initilizerProduct(self):
        productFileName = open('product.txt','r')
        for line in productFileName:
            row=line.strip().split(',')
            a=self.searchCategory(row[1].lower())
            self.createProduct(row[0].lower(),a,row[2].lower(),row[3])
        productFileName.close()
      
    def __initilizerUser(self):
        userFileName = open('user.txt','r')
        for line in userFileName:
            row=line.strip().split(',')
            if row[0]=='staff':
                self.createStaff(row[1],row[2])
            elif row[0]=='member':
                self.createMember(row[1],row[2],row[3],row[4])
        userFileName.close()

    def guestGetRegistered(self,mName: str, mPhone: str, mEmail: str,mPassword: str) -> str:
        # Guest Registered as a Member, first to check if it is already in the member list
        aCart=ShoppingCart()
        aMember=Member(mName,aCart,mPhone,mEmail,mPassword)
        aMember.myShoppingCart=self.cart
        for member in self.allMembers:
            if aMember.memberEmail==member.memberEmail:
                raise BadRequestError ('Member already exist, please log in')
            else:
                self.allMembers.append(aMember)
                return aMember
     
        
              
    def createStaff(self,sName: str,  sPassword: str):
        # Creates an instance of Staff
        aStaff=Staff(sName, sPassword)
        self.allStaff.append(aStaff)
        
    def createMember(self,cname:str, cphone:str,cemail:str,cpassword:str):
        aCart=ShoppingCart()
        aMember=Member(cname, aCart,cphone,cemail,cpassword)
        self.allMembers.append(aMember)
        return aMember  
        

   

    def createProduct(self,prodName,prodCategory,prodDescrip,prodPrice):
        aProduct=Product(prodName,prodCategory,prodDescrip,prodPrice)
        self.allProducts.append(aProduct)
        

                
    def searchCategory(self,cateName) -> Category:
        for category in self.allCategories:
            if category.categoryName==cateName:
                return category

                

    def searchProductByName(self,pName: str) -> Product:
        # Find Product based on a given product name
        for product in self.allProducts:
            if product.productName==pName:
                return product


    def searchProductByName2(self,pName: str):
        # Find Product based on a given product name
        for product in self.allProducts:
            if product.productName==pName:
                return product.productName            



    def searchProductByCategory(self,pCategory: str) -> Product:
        # Find Products based on a given product category
        prodNameList=[]
    
        aCategory=self.searchCategory(pCategory)
        if aCategory==None:
            raise BadRequestError('Category not found')  
        else:
            for product in aCategory.getProductList():
                prodNameList.append(product.productName)
            if len(prodNameList)==0:
                raise BadRequestError('No product in this Category yet')
            else:
                return prodNameList
         
    
        


    def searchMember(self,memberName):
        if memberName=='guest':
            return self.guest
        else:    
            for member in self.allMembers:
                if member.memberName==memberName:
                    return member
        



    def searchStaff(self,staffName):
        for staff in self.allStaff:
            if staff.staffName==staffName:
                return staff
            else:
                return None

    def staffLogIn(self,sName: int, sPassword: str) -> str :
    #    Staff use name and password to log in
    # If name and password match, redirect to the staff Page, 
    # if not, indicate user to input correct name and password
        for staff in self.allStaff:
            if staff.staffName==sName and staff.staffPassword==sPassword:
                return staff
            else:
                raise BadRequestError('User name and password does not match')
        

    def memberLogIn(self,mName: str, mPassword: str) -> str :
        # Member use name and password to log in
        for member in self.allMembers:
            if member.memberName==mName and member.memberPassword==mPassword:
                # member.myShoppingCart=self.cart
                return member
        else:
            raise BadRequestError('User name and password does not match')

    def viewAllProducts(self) -> str:
        productList=[]
        for product in self.allProducts:
            productList.append(product.productName)
        return productList

    def viewProductDetails(self,pName: str) -> Product:
        for product in self.allProducts:
            if product.productName==pName:
                return product

    def displayProducts(self):
        allProducts=[]
        for product in self.allProducts:
            allProducts.append(product.displayProduct())
        return allProducts

    def addItem(self, customerName: str ,pName: str) -> str:
        # Add a Product to a Member/Guest's shopping Cart,if it is a guest, create a guest object and its shoppingcart
        aProduct=self.searchProductByName(pName)
        # if len(self.allMembers)!=0:        
        aMember=self.searchMember(customerName)
        aMember.addItem(aProduct)
        return True
            


    def removeItem(self,customerName: str, pName: str) -> str:
        # Remove a Product from a Member/Guest's shopping Cart
        # aProduct=self.searchProductByName(pName)
        aMember=self.searchMember(customerName)
        for item in aMember.myShoppingCart.allItems:
            if item.itemProduct.productName==pName:
                anItem=item
                aMember.removeItem(anItem)



    def viewCart(self,customerName: str ) -> str:
        if customerName != 'guest':
            return self.searchMember(customerName).viewCartDetails()
            
        else:
            return self.guest.viewCartDetails()
           
    def getSubTotal(self,customerName:str):
        aMember=self.searchMember(customerName)
        return '$'+str(aMember.myShoppingCart.getTotalSum())
    
    def emptyCart(self,customerName):
        aMember=self.searchMember(customerName)
        aMember.emptyCart()

    
    def placeOrder(self,dateCreated: date,memberName:str, ) -> str:
        # Create a Order Object and append it to the member's Order List
        # First to use the cName to check if it is a member, if yes, create a Order Object,also create a Payment Object,a Address Objects,if billing and delivery not the same, 2 address objects
        # Also, need to call shopping cart checkout function to clear the shopping cart
        aMember=self.searchMember(memberName)
        aOrder=Order(dateCreated,aMember)
        Staff.allCustomerOrders.append(aOrder)
        amount=aOrder.calOrderTotalAmount()
        orderID=aOrder.orderID
        return aOrder,amount,orderID
    
    def searchOrder(self,orderID:int):
        for order in Staff.allCustomerOrders:
            if order.orderID==orderID:
                return order
            else:
                return False

    def updateDeliveryAddress(self,street,suburb,city,postcode,aOrder:Order):
        anAddress=Address(street,suburb,city,postcode)
        aOrder.deliveryAddress=anAddress
        return anAddress



    def updateCCPayment(self,amount,ccNumber,ccExpired,ccHolder,CVC,aOrder:Order):
        if len(ccNumber)!=16:
            raise BadRequestError('Card number must be 16 digital')
        if len(CVC)!=3:
            raise BadRequestError('CVC must be 3 digital')
        else:
            aCCPayment=CCPayment(amount,ccNumber,ccExpired,ccHolder,CVC)
            aOrder.orderPayment=aCCPayment
            return aCCPayment

    def updateBankPayment(self,amount,bankNumber,accountOwner,aOrder:Order):
        aBankPayment=BankPayment(amount,bankNumber,accountOwner)
        aOrder.orderPayment=aBankPayment
        return True    
            


    def cancelOrder(self, orderID:int, memberName:str ) -> str:
        # Cancel order if order status is processing, awaiting shipment
        aMember=self.searchMember(memberName)
        aOrder=aMember.searchOrder(orderID)
        if aMember.cancelOrder(aOrder):
        # if aOrder.orderStatus in ['processing','awaiting shipment']:
        #     aOrder.orderStatus='cancelled'
            message=f'Order has been cancelled'
            return message     
        else:
            message=f'Order cannot be cancelled ,either it has been shipped or delivered or already cancelled'
            return message              
    
    def viewOrder(self,orderID:int, memberID:int):
        for member in self.allMembers:
            if member.memberID==memberID:
                aMember=member
        for order in aMember.allMyOrders:
            if order.orderID==orderID:
                return order
            else:
                return False    


    def memberViewAllOrders(self,memberName:str ) -> str:
        # Member view all his order history
        for member in self.allMembers:
            if member.memberName==memberName:
                return member.viewAllMyOrders()

    

    def staffViewOrders(self,sname) -> str:
        for staff in self.allStaff:
            if staff.staffName==sname:
                aStaff=staff
        return aStaff.staffViewOrders()

    def updateOrderStatus(self, ordID: str, sname:str ,newStatus) -> str:
        for staff in self.allStaff:
            if staff.staffName==sname:
                aStaff=staff
        for order in aStaff.allCustomerOrders:
            if order.orderID==ordID:
                anOrder=order
        anOrder.orderStatus=newStatus
        return True        


    def generateReport(self, smonth, sname: str) -> str:
        aStaff=self.searchStaff(sname)
        orderList=[]
        for order in aStaff.allCustomerOrders:
            month=datetime.strptime(order.dateCreated, "%Y-%m-%d").month
            if int(month)==smonth:
                orderList.append(order.showOrderDetails())
        return orderList                


    # create some order objects to test staff functionality
    def assemble_order(self):
        orderFileName = open('order.txt','r')
        lines=orderFileName.readlines()
        row1=lines[0].split(',')
        row2=lines[1].split(',')
        row3=lines[2].split(',')
        row4=lines[3].split(',')
        cate1=Category(row1[1].rstrip().lower())
        prod1=Product(row1[0],cate1,row1[2],row1[3])
        aCart=ShoppingCart()
        member1=Member(row3[0],aCart,row3[1],row3[2],row3[3])
        member1.addItem(prod1)
        order1=Order('2022-10-01',member1)
        address1=Address(row2[0],row2[1],row2[2],row2[3])
        bpayment1=BankPayment(row4[0],row4[1],row4[2])
        order1.deliveryAddress=address1
        order1.orderPayment=bpayment1
        member1.addItem(prod1)
        member1.addItem(prod1)
        order2=Order('2022-11-02',member1)
        Staff.allCustomerOrders.append(order1)
        Staff.allCustomerOrders.append(order2)
        orderFileName.close()