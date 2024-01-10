'''
File Name: prog1.py
Author: Austin Ring
Major: Computer Science
Date: 2/18/23
Purpose: Input Income and Expenses to Give Remaining Balance For the Month
'''

#Name is asked so it can be used at the end of the program
name = input("\nEnter Your Name: ")
print("Hello, ",name)

'''
--This section is where you input the income and the bills for the month.
--All variables are floats to ensure cents are accounted for.
'''
income = float(input("\nPlease enter your monthly income: $"))
print("\nPlease Enter Your Monthly Expenses Below!\n")
rent = float(input("Enter your Monthly Rent: $"))
water = float(input("Enter your Monthly Water Bill: $"))
phone = float(input("Enter your Monthly Phone Bill: $"))
internet = float(input("Enter your Monthly Internet Bill: $"))
car = float(input("Enter your Monthly Car Paymont: $"))
gas = float(input("Enter your Monthly Gas Cost: $"))
other = float(input("Enter your Other Monthly Expenses: $"))

'''
--totalExpenses is all the bills added together, and it is subtracted
  for the income to give the final balance for the month.
--If the final balance is negative (income-totalExpenses<0), a
  message will print that says you need to be better.
--If the final balance is positive or equal to zero (income-totalExpenses>=0),
  a "Good Job" will be printed
'''
totatExpenses = rent+water+phone+internet+car+gas+other
print("\n",name, ", you have $", income-totatExpenses, " remaining in your account")
if (income-totatExpenses)<0:
    print("You have no more money left this month! You should manage your money better!")
else:
    print("Good Job this month!")