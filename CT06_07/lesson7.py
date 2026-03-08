print("Hello from lesson 7")

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"


# print("Average score for " , student_name , " is: " , (round(average_score,2) ) )
 
#  ## Task 1: For Loop: 1 to 10 using range(start, stop)

# # Use a 'for' loop to print numbers from 1 to 10.

# for i in range(1,11,1):
#     print(i)
    

# ## Task 2: Even Numbers 2-20 Loop using
# ##         range(start, stop, step)

# # Print all even numbers between 2 and 20 using a 'for' loop and
# # range().

# for count in range(2,21,1):
#     print(count)

# ## Task 3: Countdown From 10 For Loop

# # Use a 'for' loop and range() to count down from 10 to 1.

# for count in range(100,0,-1):
#     print(count)

## Task 4: Word Repetition Input Loop

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger


# word = input("what word would you like repeat?")
# numberOfTimes = input("how many times would you lie to repeat?")
# numberOfTimes = int(numberOfTimes)

# for abc in range(numberOfTimes):
#     print(word)

## Task 5: Personalized Greeting Loop

# Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# Nice to meet you, burger

# name = input("what is your name?")
# times = input("how many times")
# times = int(times)
# for blah in range(times):
#     print("nice to meet you" , name)

## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19 

# num1 = input("what is the number 1?")
# num2 = input("what is the number 2?")
# num3 = input("what is the number 3?")
# num4 = input("what is the number 4?")
# num5 = input("what is the number 5?")

# total = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)

# print(total)

## Task 7: Multiplication Table Generator

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# Example:
# What number for the timestable? > << 5 >>
# output:
# 5 x 1 = 5
# 5 x 2 = 10
# ....
# ..
# 5 x 12 = 60

# number = input("what number for the timestable?")
# number = int(number)
# for i in range(1,13):
#     print(number, "x", i,"=", number * i )

## Task 8: Number Pyramid Pattern

# 1. Ask the user for a number
# 2. Using the 'for' loop, print out the number like the
#    following:

# 1
# 22
# 333
# 4444
# 55555

# Hint: You can use a code like this >>> print("a" * 5)

number = input("what number")
for bbb in range(number):
    