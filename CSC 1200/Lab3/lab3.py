'''
Date : 2/10/2023

Name : Austin Ring

Class : CSC 1200

Lab : Lab 3

Problem: Convert a Number to Binary and Printing a Number in a Triangle Pattern

Input : Part 1: Number(int) ... Part 2: Number and Character

Output : Part 1: Number Converted into Binary Representation ... Part 2: Character printed out in a triangle
'''

#par1
inputNum = int(input("Part 1.\nEnter a number: "))
binNum = ""

while(inputNum != 0):
    num1 = inputNum // 2
    rem = inputNum % 2
    binNum = str(rem) + binNum
    inputNum = num1
print(binNum)

#part2
inputNum2 = int(input("\n\nPart 2.\nEnter a number: "))
inputChar = input("Enter a character: ")
z = 0
for x in range(inputNum2):
    z = z+1
    for y in range(z):
        print(inputChar, end="")
    print("\n")