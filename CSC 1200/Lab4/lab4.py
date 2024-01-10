'''
Date : 2/10/2023

Name : Austin Ring

Class : CSC 1200

Lab : Lab 4

Problem: Calculator
'''
num1 = 0
num2 = 0
def main(choice):
    num1, num2 = getData()
    match choice:
        case 1:
            add(num1, num2)
        case 2:
            sub(num1, num2)
        case 3:
            mult(num1, num2)
        case 4|5:
            div(num1, num2)
        case 6:
            mod(num1, num2)
        case 7:
            choice = 7
        case _:
            print("Invalid Response") 

def getData():
    if choice == 4:
       num1 = float(input("First Number: "))
       num2 = float(input("Second Number: "))
    else: 
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
    return num1, num2;
def add(num1, num2):
    print(num1," + ",num2," = ",num1 + num2)
def sub(num1, num2):
    print(num1," - ",num2," = ",num1 - num2)
def mult(num1, num2):
    print(num1," * ",num2," = ",num1 * num2)
def div(num1, num2):
    print(num1," / ",num2," = ",num1 / num2)
def mod(num1, num2):
    print(num1," % ",num2," = ",num1 % num2)

choice = 0

while choice != 7:
    print("Welcome to the calculator!")
    print("\t1. Add\n\t2. Subtract\n\t3. Multiply\n\t4. Float Division\n\t5. Integer Division\n\t6. Mod\n\t7. Quit")
    choice = int(input("What do you want to do? "))
    if choice != 7:
        main(choice)
    