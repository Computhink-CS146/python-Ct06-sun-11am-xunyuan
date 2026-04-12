print("Hello from lesson 9")
# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()'
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'
# import random

# num1 = random.randint(1,6)
# print("1st number = " , num1)
# num2 = random.randint(1,6)
# print("2nd number = " , num2)
# num3 = random.randint(1,6)
# print("3rd number = " , num3)
# all_even_odd =  (num1%2== 0) ==(num2%2==0) == (num3%2==0)
# print("all numbers are even/odd:", all_even_odd)
# # ---------------------------------------------------------------
# # Task 4: Fruits Shop
# **Task 4a**:
# Draw out the flowchart (on a draw.io) of a program for
# the fruit shop, "FruitiFresh". FruitiFresh sells 2 fruits,
# Apple & Orange with the following pricing scheme:

# Apple:
# 1 Apple = 60 cents
# If buy more than 5 apples, get 10% discount for all apples

# Orange:
# 1 Orange = 90 cents
# If buy more than 5 oranges, get 10% discount for all oranges

# You want to create a program that:
# 1. Asks the user for the number of apples and oranges they
#    want to buy.
# 2. Print total price of the fruits

# **Task 4b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

apple = input("how many apples do you want to buy?")
orange = input("how many oranges do you want to buy?")

apple = int(apple)
orange = int(orange)
if apple > 5:
    costApple = apple * 0.60 * 0.9
else:
    costApple = apple * 0.60

if orange > 5:
    costOrange = orange * 0.90 *0.9
else :
    costOrange = orange *0.9

total = costApple + costOrange

print(total)