import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

from category import Category
from product import Product
from item import Item
from shoppingCart import ShoppingCart


cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
aCart=ShoppingCart()



def test_addItem():
    aCart.addItem(book1)
    assert len(aCart.allItems)==1
    aCart.addItem(book1)
    assert aCart.allItems[0].quantity==2
    aCart.addItem(book2)
    assert len(aCart.allItems)==2
    assert aCart.allItems[1].quantity==1

def test_viewCartDetails():
    assert aCart.viewCartDetails()==[('It',2,50.0),("Dune",1,28.0)]    


def test_getTotalSum():
    # total 2 items: 25.0*2+28.0=78.0
    assert aCart.getTotalSum()==78.0   



def test_removeItem():
    item1=aCart.allItems[1]
    aCart.removeItem(item1)
    assert len(aCart.allItems)==1



def test_emptyCart():
    aCart.emptyCart()
    assert len(aCart.allItems)==0
