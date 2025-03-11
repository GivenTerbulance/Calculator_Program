#Mini-Calculator
"""
Author : Given Teboho Ikaneng
Date: 11/03/2025

"""

num1 = int(input("Please enter num1:"))
num2 = int(input("Please enter num2:"))
operator = str(input("Input operator:"))

def sum():
    sum = num1 + num2
    return sum 

def sub():
    sub = num1 - num2
    return sub

def mul():
    mul = num1 * num2
    return mul

def qou():
    qou = num1 / num2
    return qou

if operator == "+":
    print("The addition of", num1 ," "+"and", num2 ," "+"is",sum())
elif operator == "-":
    print( "The difference of", num1 ," "+"and", num2 ," "+"is",sub())
elif operator == "*":
    print( "The product of", num1 ," "+"and", num2 ," "+"is",mul())
elif operator == "/":
    print( "The qoutient  of", num1 ," "+"and", num2 ," "+"is",qou())
else: 
    print("Invalid operator, Try / or + or - or *")
