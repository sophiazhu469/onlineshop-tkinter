import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)



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
from onlineshop import OnlineShop



aShop=OnlineShop()
aCart=ShoppingCart()


def test_createCategory():
    aShop.createCategory('phone')
    assert len(aShop.allCategories)==5


def test_createStaff():
    aShop.createStaff('sam','rt')
    assert len(aShop.allStaff)==3


def test_createMember():
    aShop.createMember('Matt','02345666','ma@gamil.com','ddd')
    assert len(aShop.allMembers)==2

def test_createProduct():
    cate1=Category('laptop')
    aShop.createProduct('HP laptop',cate1,'touchscreen laptop',1200)
    assert len(aShop.allProducts)==12



def test_searchCategory():
    assert aShop.searchCategory('book').categoryID== 401

def test_searchProductByName():
    assert aShop.searchProductByName('zelda').productID==505

def test_searchProductByName2():
    assert aShop.searchProductByName2('zelda')=='zelda'

def test_searchProductByCateggory():
    assert aShop.searchProductByCategory('game')==['paper mario','zelda','ring fitness']


def test_searchMember():
    assert aShop.searchMember('Oliver').memberID==300

def test_searchStaff():
    assert aShop.searchStaff('Sophia').staffID==100


def test_staffLogin():
    assert aShop.staffLogIn('Sophia','s').staffID==100

def test_memberLogin():
    assert aShop.memberLogIn('Oliver','a').memberID==300  

def test_viewAllProducts():
    assert len(aShop.viewAllProducts())==12         

def test_viewProductDetails():
    assert aShop.viewProductDetails('zelda').productID==505

def test_displayProducts():
    assert len(aShop.displayProducts())==12



def test_guestGetRegistered():
    assert aShop.guestGetRegistered('sally','02311111','sally@gmail.com','df').memberID==302

def test_addItem():
    aMember=aShop.searchMember('Oliver')
    aShop.addItem('Oliver','zelda')
    aShop.addItem('Oliver','paper mario')
    assert len(aMember.myShoppingCart.allItems)==2
    

def test_removeItem():
    aMember=aShop.searchMember('Oliver')
    aShop.removeItem('Oliver','zelda')
    assert len(aMember.myShoppingCart.allItems)==1

def test_viewCart():
    assert aShop.viewCart('Oliver')==[('paper mario',1,99.0)]

def test_getSubTotal():
    assert aShop.getSubTotal('Oliver')=='$99.0'    

def test_emptyCart():
    aMember=aShop.searchMember('Oliver')
    aShop.emptyCart('Oliver')
    assert len(aMember.myShoppingCart.allItems)==0


def test_placeOrder():
    aShop.addItem('Oliver','zelda')
    assert aShop.placeOrder('2022-11-01','Oliver')[1]==100.0

def test_searchOrder():
    assert aShop.searchOrder(601)==False
    assert aShop.searchOrder(600).orderStatus=='processing'

def test_memberViewAllOrders():
    assert len(aShop.memberViewAllOrders('Oliver'))==1

def test_updateDeliveryAddress():
    aMember=aShop.searchMember('Oliver')
    aOrder=aMember.searchOrder(600)
    assert aShop.updateDeliveryAddress('17 Addington St','halswell','CHC','8025',aOrder).myCity=='CHC'

def test_updateCCPayment():
    aMember=aShop.searchMember('Oliver')
    aOrder=aMember.searchOrder(600)
    assert aShop.updateCCPayment(100.0,'1234555567893456','0224','Sam Y','347',aOrder).myCardCVC=='347'

def test_updateBankPayment():
    aMember=aShop.searchMember('Oliver')
    aOrder=aMember.searchOrder(600)
    assert aShop.updateBankPayment(100.0,'12346789','sam y',aOrder)==True

def test_viewOrder():
    assert aShop.viewOrder(600,300).calOrderTotalAmount()==100.0


def test_staffViewOrders():
    assert len(aShop.staffViewOrders('Sophia'))==1

def test_updateOrderStatus():
   aShop.updateOrderStatus(600,'Sophia','shipped')
   aOrder=aShop.searchOrder(600)
   assert aOrder.orderStatus=='shipped'
    

def test_generateReport():
    assert len(aShop.generateReport(11,'Sophia'))==1

def test_cancelOrder():
    aShop.addItem('Oliver','paper mario')
    aShop.placeOrder('2022-11-02','Oliver')
    aShop.cancelOrder(601,'Oliver')
    aMember=aShop.searchMember('Oliver')
    aOrder=aMember.searchOrder(601)
    assert aOrder.orderStatus=='cancelled'

def test_assemble_order():
    aShop.assemble_order()
    # as above test functions already create 2 orders, and in the assemble_order functions, 2 orders have been created.
    assert len(Staff.allCustomerOrders) ==4   