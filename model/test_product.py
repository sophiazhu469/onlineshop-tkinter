import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)


from product import Product
from category import Category

def test_displayProduct():
    cateBook=Category('book')
    book1=Product('It',cateBook,'A horror story by Stephen King',25)
    assert book1.displayProduct()=='It:$25'