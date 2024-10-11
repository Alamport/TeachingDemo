"""
File: simple_calculator.py
Author: Adin Lamport
Date: 3/27/24
Description: A simple calculator able to do various mathematical operations
Topics:
        - Functions
        - Conditionals
        - Basic Recursion
"""
import math

calculations = []
op_two_nums = ["+", "-", "*", "/"]
other_op = ["sqrt", "C", "AC", "M-", "M+"]

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
        
def store(result):
    calculations.append(result)

def recall():
    return calculations.pop()

def sqrt(num):
    return math.sqrt(num) 

def reset():    # represents C operation
    pass

def hard_reset():       # represents AC operation
    for i in range(len(calculations)):
        recall()

def two_nums_op(num1, num2, op):
    pass

def one_num_op(num):
    pass

def main():
    while True:
        op = input("What operation? (+ | - | / | * | sqrt | C | AC | M- | M+): ")

        if op in op_two_nums:
            num1 = input("First Number: ")
            num2 = input("Second Number: ")
            result = two_nums_op(num1, num2, op)
        elif op in other_op:
            num = input("Number")
            result = one_num_op(num)
            

# def store():
#         pass

# def recall():
#         pass

# def sqrt():
#         pass

# def reset():    # represents current operation
#         pass

# def shut_down():
#         pass

# def main():
#         num1 = int(input("Enter a number: "))
#         num2 = int(input("Enter a second number: "))
#         operation = input("Enter an operation (+|-|*|/) ")

#         if operation == '+':
#                 print(addition(num1, num2))
#         elif operation == '-':
#                 print(subtraction(num1, num2))
#         elif operation == '*':
#                 print(multiplication(num1, num2))
#         elif operation == '/':
#                 print(division(num1, num2))
#         else:
#                 print("Try again and enter an operation that is correct")

# main()