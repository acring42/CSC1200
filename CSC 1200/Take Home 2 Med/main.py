'''
Date : 3/24/2023

Name : Austin Ring

Class : CSC 1200

Assignment: Take Home Excersises 2 Medium

Problem: Set of small python programs
'''

def boolValue():
    value = input("Enter True or False: ")
    if value == "True":
        value=1
    else:
        value=0
    print(value, "\n")

def loopInputInt():
    for x in range(10):
        print(int(input("Please enter an integer: ")), "\n")

def loopInputFloat():
    x=0
    while x<10:
        print(float(input("Please enter an float: ")), "\n")
        x+=1

def stringTest():
    myStr = "This is test"
    myStr = "***" + myStr + "***"
    print(myStr, "\n")

def multiply():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print((a+b)*(a+b), "\n")

def loopList():
    myList = [1,2,3,4,5]
    for x in myList:
        print(x)
    value = int(input("Enter a number: "))
    if value in myList:
        print("This number is in the list", "\n")
    else:
        print("This number is not in the list\n")

def dictionary():
    dictName = {"name1":"20","name2":"44","name3":"33"}
    print(dictName)

def gcd():
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    while(b!=0):
        a, b=b, a%b
    
    print("\nThe Greatest Common Denominator is ",a ,"\n")

def date():
    import datetime
    start = datetime.datetime(2023,3,7,8,0)
    end = datetime.datetime(2023,3,7,9,0)

    current = start
    while current <= end:
        print(current, "AM")
        current += datetime.timedelta(minutes=1)

def osInfo():
    import os
    import platform
    print("\n",os.name)
    print(platform.system())
    print(platform.release())

def tryExcept():
    x=12
    print("We are setting X=12, and we are going to try to print it along with Y which doesn't exist")
    try:
        print(x)
        print(y)
    except:
        print("Something went wrong!")

def main():
    boolValue()
    loopInputInt()
    loopInputFloat()
    stringTest()
    multiply()
    loopList()
    dictionary()
    gcd()
    date()
    osInfo()
    tryExcept()

main()