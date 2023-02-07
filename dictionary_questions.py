# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:19:18 2023

@author: ZZ0AVD820
"""

# Question 1
# Can you remember how to check if a key exists in a dictionary?
# Using the capitals dictionary below write some code to ask the user to input
# a country, then check to see if that country is in the dictionary and if it is
# print the capital. If not tell the user it's not there.
# '''

# capitals = {'France':'Paris', 'Spain':'Madrid', 'Poland':'Warsaw', 
#             'Germany':'Berlin', 'England':'London', 'Italy':'Rome'}
# user_input = input('Enter the name of the country:\n>>> ')
# if user_input in capitals:
#     print(capitals[user_input])
# else: print('No such country in the dictionary')

# '''
# Question 2
# Write python code that will create a dictionary containing key, value pairs
# that represent the first 12 values of the Fibonacci sequence
# i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
# '''

# k1 = 0 
# k2 = 1
# dictionary = {}
# for v in range(1,20):
#     dictionary[v] = (k1)
#     k1, k2 = k2, (k1+k2)
# print(dictionary)




# '''
# Question 3
# Create a dictionary to represent the open, high, low, close share price data
# for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
# the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
# # '''
# price_dictionary = {'Python DS':{'open':12.87, 'high':13.23, 'low':11.42, 'close':13.10},
#                     'Pythonsoft':{'open':23.54, 'high':25.76, 'low':21.87, 'close':22.33},
#                     'Pythazon':{'open':98.99, 'high':102.34, 'low':97.21, 'close':100.065},
#                     'Pybook':{'open':203.63, 'high':207.54, 'low':202.43, 'close':205.24},}
# print(price_dictionary)
                    




# '''
# Question 4
# Go to the python module web page and find a module that you like. Play with it,
# read the documentation and try to implement it.
# '''




# '''
# Question 5
# Create a dictoinary containing as keys the letters from A-Z, the values should
# be random numbers created from the random module. Can you draw a bar graph of
# the results?
# '''

# import random
# import string
# alphabet = string.ascii_uppercase
# az_dict={}
# for v in alphabet:
#     az_dict[v] = random.randint(0, 10000)
# print(az_dict)    

# import matplotlib
# x,y = zip(*az_dict.items())

# matplotlib.pyplot.bar(x,y)



# '''
# Question 6
# Create a dictionary containing 4 suits of 13 cards
# ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# '''

# cards=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# suits=['spades', 'hearts', 'diamonds', 'clubs']
# cards_dict={}
# for v in cards:
#     cards_dict[v] = suits
# print(cards_dict)


























