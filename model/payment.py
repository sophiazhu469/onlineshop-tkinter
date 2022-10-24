from abc import ABC,abstractmethod
from typing import List
from datetime import date

class Payment(ABC):
    """! The Payment Abstarct Class"""
    def __init__(self,amt: float) :
        """! The Payment Initializer"""
        self._amount = amt

    @property
    def amount(self):
        return self._amount    

class CCPayment(Payment):
    """! The Credit Card Payment Class"""
    def __init__(self,amt: float,cNumber: str):
        """! Credit Card Payment Initializer"""
        self.__myCardNumber = cNumber
        super().__init__(amt)

    @property
    def myCardNumber(self):
        return self.__myCardNumber    


    def __str__(self):
        return self._amount + ' ' + self.__myCardNumber    





class BankPayment(Payment):
    """! The Bank Account Payment Class"""
    def __init__(self, amt: float, bnumber: str):
        """! Bank Account Payment Initializer"""
        self.__myBankNumber = bnumber
        super().__init__(amt)


    @property
    def myBankNumber(self):
        return self.__myBankNumber        


    def __str__(self):
        return self._amount + ' ' +self.__myBankNumber    