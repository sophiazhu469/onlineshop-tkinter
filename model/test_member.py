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

def test_memberLogin():
    pass

def test_viewAllMyOrders():
    pass

def test_addOrder():
    pass


def test_cancelOrder():
    pass

def test_trackMyOrderStatus():
    pass

def test_checkout():
    pass

def test_makePayment():
    pass

def test_addDeliveryAddress():
    pass