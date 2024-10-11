"""
calc_test.py
Author(s): Adin Lamport
Last Modified: 10/11/2024
Tests whether one's calculator works properly
"""
import simple_calculator as calc

assert(calc.addition(1,2) == 3)
assert(calc.addition(5,-2) == 3)
assert(calc.addition(-2, -5) == -7)
assert(calc.addition(1.5, 3.2) == 4.7)
assert(calc.addition("Learn", " Python") == "Learn Python")
print(f"Passed Addition Tests")

assert(calc.subtraction(1,2) == -1)
assert(calc.subtraction(5,-2) == 7)
assert(calc.subtraction(-2, -5) == 3)
print(f"Passed Addition Tests")