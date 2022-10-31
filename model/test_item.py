import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)

from category import Category
from item import Item
from product import Product


def test_calculateTotal():
    cateBook=Category('book')
    book1=Product('It',cateBook,'A horror story by Stephen King',25)
    item1=Item(book1,3)
    assert item1.calculateTotal()==75


