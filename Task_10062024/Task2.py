import math

# Task #2
#
# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

number = int(input("Enter a Number : "))
print(f"Square of Number :  {number**2}",f"cube of number : {math.pow(number,3)}")


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
first_number=int(input("Enter first number : "))
second_number=int(input("Enter second number : "))
print(f"first Number : {first_number} Grater than second number : {second_number}" if first_number>second_number else f"Second Number : {second_number} Grater than First Number : {first_number}" if first_number<second_number else "Numbers are equal")