import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)


from guest import Guest
from customer import Customer
from shoppingCart import ShoppingCart
from category import Category
from product import Product
from item import Item
from member import Member

cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
aCart=ShoppingCart()
aGuest=Guest('guest',aCart)
print(aGuest.guestName)

def test_register():
    aGuest.addItem(book1)
    aMember=aGuest.register('sophia','02111111','s@gmail.com','s')
    # guest shopping cart's item transfer to member's cart after register
    assert len(aMember.myShoppingCart.allItems)==1
