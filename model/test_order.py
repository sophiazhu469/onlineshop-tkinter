import pytest
import sys
import os

project_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if project_path not in sys.path:
    sys.path.append(project_path)


from member import Member
from address import Address
from payment import Payment

def test_calOrderTotalAmount():
    pass
