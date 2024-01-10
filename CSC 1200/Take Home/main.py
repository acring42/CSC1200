'''
Date : 2/15/2023

Name : Austin Ring

Class : CSC 1200

Lab : Take Home Exercises 

Problem: Type Conversion, Area of a Triangle, List Operations, Temperature Conversion, Multiplication Table, Factorial
'''

def typeconv(input):
    print("Type Conversion") 
    if input.isdigit():
        num = int(input)
    else:
        num = float(input)
    print("Type: ", type(num))

def areaTriangle():
    print("Area of a Triangle\n")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of a Triangle: ", (0.5*base)*height)

def listoperations():
    print("List Operations")
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,10]
    list3 = list1 + list2
    print(list3)
    list1.insert(0,0)
    print(list1)
    list2.append(11)
    print(list2)
    print(len(list1))
    print(len(list2))
    list1.reverse()
    print(list1)
    print(list1[len(list1)-1])
    print(list2[len(list2)-1])

def tempconvert(temp):
    print("Celcius to Fahrenheit: ", (temp*1.8)+32)

def multitable(input):
    print("Multiplication Table")
    for x in range(10):
        print(input, " * ", x+1, " = ", input*(x+1))

def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num-1)

def main():
    typeconv(input("Enter a string: "))
    areaTriangle()
    listoperations()
    tempconvert(float(input("Enter Celcius: ")))
    multitable(int(input("Enter a number: ")))
    print("Factorial\n")
    num = fact(int(input("Enter a number: ")))
    print(num)

main()