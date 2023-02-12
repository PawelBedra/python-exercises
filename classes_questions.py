# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:42:36 2023

@author: ZZ0AVD820
"""
'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

# class Bank_acc(object):
#     '''
#         Attributes
#         ----------
        
#     '''
#     def __init__(self, balance=0.0):
#         self.balance = balance
#         print(f'Constructor info: your new balance is ${self.balance}')
        
#     def deposit(self, depo):
#         self.balance += depo
#         print(f'Deposit info: your new balance is ${self.balance}')
        
#     def withdraw(self, draw):
#         self.balance -= draw
#         print(f'Withdrawal info: your new balance is ${self.balance}')

# paul_acc = Bank_acc(1000.00)
# paul_acc.deposit(200)
# paul_acc.withdraw(500)



# '''
# Question 2
#   Create a circle class that will take the value of a radius and
#   return the area of the circle
# '''

# import math
class Circle(object):
    '''Docstring here'''
    
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        import math
        area = math.pi * (self.radius ** 2)
        print(f'Area of the circle is {area}')
        return area
        
        
            

















