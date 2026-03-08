# ============================================================
# Q2. Savings Simulator
# ============================================================
# You are building a small savings simulator.
# A person starts with a certain amount of money.

# Every day, the person saves more money than the previous day:

# Day 1 → save $1
# Day 2 → save $2
# Day 3 → save $3
# Day 4 → save $4
# … and so on

# The program must:
# - Ask for the starting amount of money.
# - Ask for the number of days.
# - For each day, add the correct savings amount.
# - Print the total money after each day.
# - Finally, print the final total amount.

# Program Requirements:
# - Use a for loop.
# - Use range() correctly.
# - Update the total amount inside the loop.
# - Print exactly in this format:
#     Day <X>: $<Y>
# - After the loop, print:
#     Total amount saved = $<Z>

# Note:
# - Follow the input order exactly as shown in the Test Cases.
# - You must get the correct output for ALL 3 test cases.

# ============================================================
# """

# # ============================================================
# # Step 1: Ask for Starting Amount
starting_money = input("how much money do you have?")
starting_money = int(starting_money)
NumberOfDays = input("how many days?")
NumberOfDays = int(NumberOfDays)
for count in range(1,NumberOfDays):


    starting_money = starting_money + count
    print("day",count, "-->",starting_money)
starting_money = starting_money + NumberOfDays
print("day",NumberOfDays ,"-->", starting_money)
print("total amount of money saved: ",starting_money)
# # ============================================================

