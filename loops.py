"""
File: loops.py
Author: Adin Lamport
Date: 3/27/24
Description: Goes over the two types of loops and how to use them
Topic(s):
        - Loops
"""
def for_loop():
        print("----------")
        print("Printing 0 to 4:")
        # prints out [0, 5)
        for x in range(5):
                print(x)

        print("\nPrinting 1 to 5:")
        for y in range(1, 6):
                print(y)

        print("Getting Groceries")
        groceries = ["pasta", "mozarella", "tomato sauce", "basil"]
        for item in groceries:
                print(item)

def while_loop():
        print("------------")
        print("Printing 0 to 4:")
        count = 0
        while count < 5:
                print(count)
                count += 1

        print("\nPrinting 1 to 5:")
        newCount = 1
        while newCount <= 5:
                print(newCount)
                newCount += 1

        print("Getting Groceries")
        groceries = ["pasta", "mozarella", "tomato sauce", "basil"]
        num_of_groceries = len(groceries)
        index = 0
        while index < num_of_groceries:
                print(groceries[index])
                index += 1

def main():
        print("For Loops:")
        for_loop()

        print("\n")

        print("While Loops:")
        while_loop()

main()