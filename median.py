"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        length = len(numbers)
        numbers.sort()

        if (length % 2 == 0):
            print((numbers[length//2] + numbers[length//2 - 1]) / 2) 
        else:
            print(numbers[length//2])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
