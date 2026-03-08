total = input("what is your total bill?" )
numppl = input("how many people are there?")
numppl = int(numppl)
total = int(total)
pay = total / numppl 
print("Each person pays:$ ", (round(pay ,2)))