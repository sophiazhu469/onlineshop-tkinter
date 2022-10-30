from abc import ABC
from typing import List
from datetime import date


# User Abstract Class
class User(ABC):
    def __init__(self, name='None'):
        self._userName = name