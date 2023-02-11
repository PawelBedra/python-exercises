# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:48:47 2023

@author: ZZ0AVD820
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''
# def sum_two(a,b):
#     return a+b




'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''
# def multiply(a, b=2):
#     return a * b

# print(multiply(5,6))
# print(multiply(5))



'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''
# def power(a,b=2):
#     return a ** b
# print(power(2,5))
# print(power(2))

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''
# f = open('capitals.txt', 'w')
# f.write('Warsaw, London, Berlin, Madrid, Rome, Paris')
# f.close()
# f = open('capitals.txt', 'r+')
# # content = f.read()
# print(f.read())
# f.close()


'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
# '''

# with open('capitals.txt', 'a') as f:
#     f.write(input('Enter a capital name:\n>>> '))
    
# with open('capitals.txt', 'r') as f:
#     print(f.read())




# '''
# Question 6
# Write a function that will copy the contents of one file to a new file.
# '''
with open('capitals.txt', 'r') as f:
    with open('capitals_2.txt', 'w') as g:
        g.write(f.read())
        
        




