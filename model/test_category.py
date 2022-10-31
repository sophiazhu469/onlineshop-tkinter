import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

print(sys.path)
print(os.path)
print(project_path)

from category import Category
from product import Product


cateBook=Category('book')
book1=Product('It',cateBook,'A horror story by Stephen King',25)
book2=Product('Dune',cateBook,'A book from Frank Herbert',28)
print(len(cateBook.productList))
print(cateBook.countProducts)



def test_getProductList():
    assert cateBook.getProductList()==[book1,book2]


def test_countProducts():
    assert cateBook.countProducts()==2


def test_addProduct():
    count=len(cateBook.productList)
    cateBook.addProduct(book1)
    # as when create book1 object, already called addProduct function  #
    # so it has already been added, when add it again, it does not increase #
    assert count==2
    