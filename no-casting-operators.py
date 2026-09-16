"""Numbers, Casting & Operators
Take two numbers as input and perform all arithmetic operations.

Check whether a number is even or odd using the modulus operator.

Calculate the area and circumference of a circle using its radius.

Convert temperature from Celsius to Fahrenheit.

Calculate the simple interest using principal, rate, and time.

Take a three-digit number and calculate the sum of its digits.

Demonstrate the difference between /, //, %, and ** using two numbers.

Find the largest of three numbers using comparison and logical operators."""
num1 = int(input("enter 1st num :  "))
num2 = int(input("enter 2nd num  : "))
print(f"addition / sum of {num1} and {num2} is :  " , num1 + num2)
print(f"division  of {num1} and {num2} is :  " , num1 / num2)
print(f" product / multiplication {num1} and {num2} is :  " , num1 * num2)
print(f"difference / subtraction of {num1} and {num2} is :  " , num1 - num2)

if num1 % 2== 0 :
    print(f" number {num1}  is even")
else :
     print(f" number {num1}  is odd")

""" calculation of circle """
pi = 3.14
radius = float(input("enter radius of circle "))
areaofcir = pi*(radius*radius)
print(f"area of circle is {areaofcir}")
cirofcir = 2*pi*radius
print(f"circumferenc  of circle is {cirofcir}")

""" conveting  celsius  to farhneheit """
celsius = float(input("enter the celsius "))
far = (celsius*9/5)+32
print(f"{celsius} celsius = {far} farehneheit")
""" conveting farhneheit to celsius """
far1 = float(input("enter the farhenehiet "))

cel1 = (far1 - 32)* 5/9
print(f"{far1} farehneheit = {cel1} celsius")

""" calculating simple interest usin rate principal and time """
print("calculating simple interest")
p = float(input("enter principal : "))
r = float(input("enter rate : "))
t = float(input("enter time : "))
simpleI = (p * r * t) / 100
print("simple interest is ",simpleI)
Tdignum = int(input("enter three digit whole number : "))
x = Tdignum % 10
y = (Tdignum // 10 ) % 10
z = Tdignum // 100
print(f"sum of three digit is ", x + y + z)
"""demontrating the difference between with example / , //, % """
print("enter values to domenstrate / , // , %")
a1 = int(input("enter value for a1 : "))
b1 = int(input("enter value for b1 : "))
print(a1/b1,f" means {a1} / {b1} : this  / is for division ")
print(a1+b1,f"means {a1} // {b1} this // is to get whole value  ") #if 5 // 2 output will be  2 not 2.5
print(a1%b1, f" means {a1} %{b1}  this %  modulo used to get reminder value " )#eg 5 % 2 we get only 5 that 2.5 0.5 value 









