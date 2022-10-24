from abc import ABC,abstractmethod
from typing import List
from datetime import date


# User Abstract Class
class User(ABC):
    def __init__(self, name: str='None'):
        self._userName = 'None'