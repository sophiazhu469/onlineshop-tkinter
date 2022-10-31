import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

from datetime import date
from member import Member
from address import Address
from payment import Payment
from shoppingCart import ShoppingCart
from order import Order
from category import Category
from product import Product

aCart=ShoppingCart()
cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
aCart.addItem(book1)
aCart.addItem(book1)
aCart.addItem(book2)
aMember=Member('sophia',aCart,'02111111','s@gmail.com','s')
aOrder=Order('2022-10-01',aMember)

def test_set_constructor():
    assert aOrder.orderID==600
    assert aOrder.dateCreated=='2022-10-01'
    assert aOrder.orderStatus=='processing'
    assert len(aMember.allMyOrders)==1
    # pass shopping cart items to order line,so 2 items in allOrderItem
    assert len(aOrder.allOrderItems)==2
    # after pass item to orderline, shopping cart clear and become empty
    assert len(aMember.myShoppingCart.allItems)==0

def test_orderPayment():
    aPayment=()

def test_showOrderLine():
    assert aOrder.showOrderLine()==[('It',2,50.0),("Dune",1,28.0)]


def test_calOrderTotalAmount():
    # 50.0+28.0 + 5.0(shipping cost)
    assert aOrder.calOrderTotalAmount()==83.0


def test_showOrderDetails():
    assert aOrder.showOrderDetails()==(600,'sophia','2022-10-01','processing',83.0)

