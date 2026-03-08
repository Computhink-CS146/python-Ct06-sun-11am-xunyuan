print("Hello from lesson 5")

# for i in range(100):
#     print("you MUST like chikin rice")
# print("YAYAYAYAYYAYAYA FREEDOMMMM")

# for g in range(100):
#     print("I LOVE CAKEE")
#     print("plss speed...i NEEEED thiss...my mama is kinda homeless")
# print("YAYAYYAYAY CAKEEEE")

# myWord = "gay"
# for letter in myWord:
#     print("give me a", letter)

# print("Lichen is", myWord)

# for count in range(60):
#     print (count)

#4a
# for count in range(1,6):
#     print(count)
#  #4b
# for count in range(51,101):
#     print (count)
# #4c
# for count in range(18,30):
#     print(count)


## Task 8: User-Defined Range Counter

# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop

# Write a 'for' loop to count from **start** to **stop**

# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.

# ---------------------------------------------------------------

# n1 = input("give me a number: ")
# n1 = int(n1)#convert
# n2 = input("give me a number: ")
# n2 = int(n2)#convert
# if n1 > n2:
#     start = n2
#     end = n1
# else:
#     start = n1
#     stop = n2

# for counter in range(start,stop):
#     print(counter)

num = 0

for char in range(10):
    num = num + char
    print(num)