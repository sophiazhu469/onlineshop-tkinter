
import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

from customer import Customer
from shoppingCart import ShoppingCart
from category import Category
from product import Product
from item import Item

cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
aCart=ShoppingCart()
aCustomer=Customer(aCart,'customer')

def test_addItem():
    aCustomer.addItem(book1)
    assert len(aCustomer.myShoppingCart.allItems)==1
    aCustomer.addItem(book1)
    assert aCustomer.myShoppingCart.allItems[0].quantity==2
    aCustomer.addItem(book2)
    assert len(aCustomer.myShoppingCart.allItems)==2
    assert aCustomer.myShoppingCart.allItems[1].quantity==1

def test_viewCartDetails():
    assert aCustomer.viewCartDetails()==[('It',2,50.0),("Dune",1,28.0)]    

def test_removeItem():
    item1=aCustomer.myShoppingCart.allItems[1]
    aCart.removeItem(item1)
    assert len(aCustomer.myShoppingCart.allItems)==1

    

def test_emptyCart():
    aCustomer.emptyCart()
    assert len(aCustomer.myShoppingCart.allItems)==0