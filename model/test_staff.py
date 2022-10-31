import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)


from user import User
from customer import Customer
from staff import Staff
from member import Member
from order import Order
from shoppingCart import ShoppingCart
from category import Category
from product import Product


staff1 = Staff('sophia','dddddd')
aCart=ShoppingCart()
cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
aCart.addItem(book1)
aCart.addItem(book1)
aCart.addItem(book2)
member1=Member('sophia',aCart,'02111111','s@gmail.com','s')
order1=Order('2022-10-01',member1)


def test_staffLogin():
    assert staff1.staffLogIn('sophia','dddddd')==True
    assert staff1.staffLogIn('sophia','a')==False
    assert staff1.staffLogIn('Rene','dddddd')==False


def test_staffAddOrder():

    staff1.staffAddOrder(order1)
    assert len(staff1.allCustomerOrders)==1

def test_staffViewOrders():
    assert staff1.staffViewOrders()==[(600,'sophia','2022-10-01','processing',83.0)]

def test_updateOrderStatus():
    staff1.updateOrderStatus(600,'shipped')
    assert order1.orderStatus=='shipped'

def test_generateOrderReport():
    assert staff1.generateOrderReport('2022-10-01','2022-10-31')==[(600,'sophia','2022-10-01','shipped',83.0)]