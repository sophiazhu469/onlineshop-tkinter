# Imports
from datetime import date
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

# from datetime import datetime
# from flask import Flask
# from flask import session
# from flask import render_template
# from flask import request
# from flask import redirect
# from datetime import date



# aCart=ShoppingCart()
# aCate=Category('Toy')
# aProd=Product('Lego',aCate,'aa',30)
# aCart.addItem(aProd)
# print(len(aCart.allItems))
class OnlineShop:
    # The OnlineShop class,Defines all the methods for the controller
    
    def __init__(self) :
        # The initialiser for OnlineShop
   
        self.allProducts: List[Product]= []
        self.allStaff: List[Staff] = []
        self.allMembers: List[Member] = []
        self.allCategories: List[Category] = []
        self.cart=ShoppingCart()
        self.guest=Guest(self.cart)
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
            # print(row[1])
            a=self.searchCategory(row[1].lower())
            # print(a)
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
        aMember=Member(mName,mPhone,mEmail,mPassword)
        for member in self.allMembers:
            if aMember==member:
                return False
                # return 'Member already exist, please log in'
            else:
                self.allMembers.append(aMember)
                return True
     
        
              
    def createStaff(self,sName: str,  sPassword: str):
        # Creates an instance of Staff
        aStaff=Staff(sName, sPassword)
        self.allStaff.append(aStaff)
        
    def createMember(self,cname:str, cphone:str,cemail:str,cpassword:str):
        aCart=ShoppingCart()
        aMember=Member(cname, aCart,cphone,cemail,cpassword)
        self.allMembers.append(aMember)  
        

    # def createGuest(self):
    #     #create an instance of guest
    #     aCart=ShoppingCart()
    #     aGuest=Guest(aCart)
    #     return aGuest,aGuest.guestName


       
        
   

    def createProduct(self,prodName,prodCategory,prodDescrip,prodPrice):
        aProduct=Product(prodName,prodCategory,prodDescrip,prodPrice)
        self.allProducts.append(aProduct)
        
    
    def createPayment(self,amount):
        aPayment=Payment(amount)
        return aPayment


    def createBankPayment(self,amount,bankNumber):
        aBankPayment=BankPayment(amount,bankNumber)
        return aBankPayment

    def createCCPayment(self,amount,CCNumber):
        aCCPayment=CCPayment(amount,CCNumber)
        return aCCPayment
    
    def createAddress(self,street:str, suburb: str, city: str,postcode: str):
        anAddress=Address(street,suburb,city,postcode)
        return anAddress

    def createShoppingCart(self):
        aCart=ShoppingCart()
        return aCart



    def makePayment(self,ordID:int, mName:str,amount):
        aPayment=self.createPayment(amount)
        for member in self.allMembers:
            if member.memberName==mName:
                aMember=member
                return aMember
        for order in aMember.allMyOrders:
            if order.OrderID==ordID:
                order.payment=aPayment
                



    def updateDeliveryAddress(self,ordID:int, mName:str,street,suburb,city,postcode):
        anAddress=self.createAddress(street,suburb,city,postcode)
        for member in self.allMembers:
            if member.memberName==mName:
                aMember=member
                return aMember
        for order in aMember.allMyOrders:
            if order.OrderID==ordID:
                order.deliveryAddress=anAddress
                
    def searchCategory(self,cateName) -> Category:
        for category in self.allCategories:
            if category.categoryName==cateName:
                return category

                

    def searchProductByName(self,pName: str) -> Product:
        # Find Product based on a given product name
        for product in self.allProducts:
            if product.productName==pName:
                return product



    def searchProductByCategory(self,pCategory: str) -> Product:
        # Find Products based on a given product category
        prodNameList=[]
        aCategory=self.searchCategory(pCategory)
        for product in aCategory.getProductList():
            prodNameList.append(product.productName)
        return prodNameList        
   
        




    def searchMember(self,memberName):
        for member in self.allMembers:
            if member.memberName==memberName:
                return member
            else:
                return self.guest   

    def searchStaff(self,staffName):
        for staff in self.allStaff:
            if staff.staffName==staffName:
                return staff
            else:
                return None    

    def viewAllProducts(self) -> str:
        productList=[]
        for product in self.allProducts:
            productList.append(product.productName)
        return productList

    def viewProductDetails(self,pName: str) -> Product:
        for product in self.allProducts:
            if product.productName==pName:
                return product


    def addItem(self, customerName: str ,pName: str) -> str:

        # Add a Product to a Member/Guest's shopping Cart,if it is a guest, create a guest object and its shoppingcart
        aProduct=self.searchProductByName(pName)
        # if len(self.allMembers)!=0:        
        aMember=self.searchMember(customerName)
        print(type(aMember))
        return aMember.addItem(aProduct)
            
        #     if aMember:
        #         aMember.addItem(aProduct) 
        #         return 'member'
        #     else:
        #         self.guest.addItem(aProduct)
        #         return 'hello'               
        # else:
        #     self.guest.addItem(aProduct)
        #     return self.cart.allItems


    def removeItem(self,customerName: str, pName: str) -> str:
        # Remove a Product from a Member/Guest's shopping Cart
        # aProduct=self.searchProductByName(pName)
        aMember=self.searchMember(customerName)
        for item in aMember.myShoppingCart.allItems:
            if item.itemProduct.productName==pName:
                anItem=item
                aMember.removeItem(anItem)

    def emptyCart(self,customerName):
        aMember=self.searchMember(customerName)
        aMember.emptyCart()


    def viewCart(self,customerName: str ) -> str:
        if customerName != 'guest':
            return self.searchMember(customerName).viewCartDetails()
            
        else:
            return self.guest.viewCartDetails()
           
    def getSubTotal(self,customerName:str):
        aMember=self.searchMember(customerName)
        return '$'+str(aMember.myShoppingCart.getTotalSum())
    
    def checkout(self,mName):
        pass
    
    def placeOrder(self,memberID:int, dateCreated: date) -> str:
        # Create a Order Object and append it to the member's Order List
        # First to use the cName to check if it is a member, if yes, create a Order Object,also create a Payment Object,a Address Objects,if billing and delivery not the same, 2 address objects
        # Also, need to call shopping cart checkout function to clear the shopping cart
        for member in self.allMembers:
            if member.memberID==memberID:
                aMember=member
        aOrder=Order(dateCreated,aMember)
        return True


    def cancelOrder(self, orderID:int, memberID:int ) -> str:
        # Cancel order if order status is processing, awaiting shipment
        for member in self.allMembers:
            if member.memberID==memberID:
                aMember=member
        for order in aMember.allMyOrders:
            if order.orderID==orderID:
                aOrder=order
        if aOrder.orderStatus in ['processing','awaiting shipment']:
            aOrder.orderStatus='cancelled'
            message=f'Order has been cancelled'
            return message
            
        else:
            message=f'Order has been shipped or delivered,cannot be cancelled'
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


    def memberViewAllOrders(self,memberID:int ) -> str:
        # Member view all his order history
        for member in self.allMembers:
            if member.memberID==memberID:
                return member.allMyOrders

    # def checkOrderStatus(self,memberID:int ) -> str:
    #     """! Member to check a Order status
    #     @param memberID The ID of the member who create the order
    #     @return a string The status of the order"""
    #     pass

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
                member.myShoppingCart=self.cart
                return member
            else:
                raise BadRequestError('User name and password does not match')
               
    
    

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


    def generateReport(self, startDate: date, endDate: date, sname: str) -> str:
        for staff in self.allStaff:
            if staff.staffName==sname:
                aStaff=staff
        for order in aStaff.allCustomerOrders:
            if order.dateCreated>=startDate and order.dateCreated<=endDate:
                return order        


aShop=OnlineShop()
# # print(len(aShop.allCategories))
# # print(len(aShop.allProducts))
# # print(len(aShop.allCategories[1].productList))
# # print(len(aShop.allStaff))
# a=[aShop.allStaff[0].staffName,aShop.allStaff[0].staffPassword]
# print(a)
# print(aShop.allStaff[0].staffName)
# b=aShop.viewAllProducts()
# print(b)

print(len(aShop.allMembers))
print(len(aShop.allStaff))
print(aShop.allMembers[0].memberName)
print(aShop.allMembers[0].memberPassword)
print(aShop.guest.guestName)
print(len(aShop.allCategories))