from operator import truediv
import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

from datetime import date
from customer import Customer
from shoppingCart import ShoppingCart
from payment import Payment,CCPayment,BankPayment
from category import Category
from product import Product
from member import Member
from order import Order
from staff import Staff


cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
aCart=ShoppingCart()
aMember=Member('sophia',aCart,'02111111','s@gmail.com','s')
aMember.addItem(book1)
aMember.addItem(book1)
aMember.addItem(book2)
aOrder=Order('2022-10-01',aMember)
# print(aOrder.orderID)
# staff1 = Staff('Oliver','dddddd')
# print(len(staff1.allCustomerOrders))
# staff1.updateOrderStatus(600,'shipped')

# print(aOrder.orderStatus)


def test_memberLogin():
    assert aMember.memberLogIn('sophia','s')==True
    assert aMember.memberLogIn('rene','r')==False
    assert aMember.memberLogIn('sophia','a')==False

def test_viewAllMyOrders():
    assert aMember.viewAllMyOrders()==[(600,'2022-10-01','processing',83.0)]

def test_addOrder():
    aMember.addItem(book1)
    aMember.addItem(book2)
    order2=Order('2022-10-31',aMember)
    # addOrder method has been called when Initializer Order object
    # therefore the len is 2.
    assert len(aMember.allMyOrders)==2
    


def test_trackMyOrderStatus():
    assert aMember.trackMyOrderStatus(aOrder)=='processing'

def test_cancelOrder():
    assert aMember.cancelOrder(aOrder)==True


def test_makePayment():
    assert aMember.makePayment(30.0)==True
