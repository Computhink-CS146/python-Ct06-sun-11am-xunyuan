print("Hello *Taskfrom lesson 8")


# Lesson 8 - Importing Libraries, Boolean & Conditions

## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
   
# -------------------------------------------------------------

# results = 1
# for count in range(1,5+1):
#     answer = input("give me a number #" + str(count) + "?")
#     results = results * int(answer)

# print("multiplication =" , results)


## Task 1: 'time' library

# * 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.
# import time
# for count in range(10,0, -1):
#     print (count)
#     time.sleep(1)
# print("explode :D")
# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.
# import time
# ccc = input("what number would you like to countdown from?")
# ccc = int(ccc)
# for count in range(ccc,0, -1):
#     print (count)
#     time.sleep(1)
# print("explode :D")

## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# import random
# print(random.randint(1,6))
# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.
# import random
# for count in range(1,21, +1):
#     print(random.randint(0,9999))
# ---------------------------------------------------------------

## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.
windy = True
print (windy)
# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# lichen = True
# gae = True
# print(lichen == gae)
# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.
# me = True
# im = False
# print(me == im)
# ---------------------------------------------------------------
## Task 4: Random Number Guessing Game

# Create a simple program to guess a random number:​
# - Create a variable called ‘random_num’ and assign a random integer between 1 to 10.​
# - Ask the user for an input 'guess'​

# Your program will check if ‘guess’ is equal to 'random_num'.​

# The output should be one of the following:​
# - If the answer is correct – output "Correct!" ​
# - If the answer is wrong – output "Wrong!​
# import random

# num1 = random.randint(1,50)
# num2 = random.randint(1,50)
# answer = input("what is " + str(num1) + " + " + str(num2))
# correct = num1 + num2
# print(answer == correct)
# # ---------------------------------------------------------------

## Task 5: Math Question Generator

# Create a simple program that generate 2 numbers
# between 1 and 50 that the user must add together.​

# Ask the user to input the answer.​

# The output should be one of the following:​
# - If the answer is correct – output "Correct!"​
# - If the answer is wrong – output "Wrong!​
# # ---------------------------------------------------------------
# ## Task 6: Random Multiplication Quiz

# Create a program that generates a certain number of
# random multiplication questions.​
# 1. Ask the user to input how many questions should be asked.​
# 2. Multiply 2 random numbers between 1 and10 and save the 'answer'.​
# 3. Ask the user to input their answer, 'user_answer'.​
# 4. Check if 'user_answer' is equal to 'answer'.

# The output should be one of the following:​
# - If the answer is correct – output "Correct!" ​
# - If the answer is wrong – output "Wrong!​

# import random
# num_question = int(input("how many question?"))
# for count in range(num_question):
#     num1 = random.randint(1,6)
#     num2 = random.randint(1,6)
#     question = "what is " + str(num1) + "x" + str(num2) + "?"
#     hidden_answer = num1 * num2
#     user_answer = int(input(question))
#     if hidden_answer == user_answer:
#         print("correct")
#     else:
#         print("wrong")