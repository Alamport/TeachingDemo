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
def addition(num1, num2):
        return num1 + num2

def subtraction(num1, num2):
        return num1 - num2

def multiplication(num1, num2):
        return num1 * num2

def division(num1, num2):
        return num1 / num2

def main():
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a second number: "))
        operation = input("Enter an operation (+|-|*|/) ")

        if operation == '+':
                print(addition(num1, num2))
        elif operation == '-':
                print(subtraction(num1, num2))
        elif operation == '*':
                print(multiplication(num1, num2))
        elif operation == '/':
                print(division(num1, num2))
        else:
                print("Try again and enter an operation that is correct")

main()