from abc import ABC,abstractmethod
from typing import List
from datetime import date
from xml.etree.ElementPath import prepare_parent

from model.badRequestError import BadRequestError

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
    def __init__(self,amt: float,cNumber: int,cExpired:str,cHolder:str,CVC:str):
        """! Credit Card Payment Initializer"""
        self.__myCardNumber = cNumber
        self.__myExpiredDate=cExpired
        self.__myCardHolder=cHolder
        self.__myCardCVC=CVC
        super().__init__(amt)

    @property
    def myCardNumber(self):
        return self.__myCardNumber

    @myCardNumber.setter
    def myCardNumber(self,value):
        if len(str(value))!=16:
            raise BadRequestError('Card Number must be 16 digital')
        else:
            self.myCardNumber=value

    @property
    def myExpiredDate(self):
        return self.__myExpiredDate

    @property
    def myCardHolder(self):
        return self.__myCardHolder

    @property
    def myCardCVC(self):
        return self.__myCardCVC                            


    def __str__(self):
        return str(self._amount) + ' ' + str(self.__myCardNumber)  

class BankPayment(Payment):
    # The Bank Account Payment Class"""
    def __init__(self, amt: float, bnumber: str,bowner):
        self.__myBankNumber = bnumber
        self.__myBankOwner=bowner
        super().__init__(amt)


    @property
    def myBankNumber(self):
        return self.__myBankNumber   

    @property
    def myBankOwner(self):
        return self.__myBankOwner         


    def __str__(self):
        return str(self._amount) + ' ' +str(self.__myBankNumber)    