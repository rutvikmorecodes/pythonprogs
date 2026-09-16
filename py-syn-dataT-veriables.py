""" Python Syntax, Variables & Data Types
Basic

Print your name, age, and college name on separate lines.

Create variables for your name, age, and percentage. Print them using an f-string.

Create two variables and  Print their sum, difference, product, and division.

Create variables of type int, float, str, bool, and list. Print their data types using type().

Take the user's name and age as input. Display a message like: Hello Rutik, you are 20 years old.

Convert a string "100" into an integer and add 50 to it.

Swap two variables without using a third variable. """

name = "rutvik kartar more" 
age = 21
#percentage  
hsc = 76.20
print(f"name of student is : {name} \n age of {name } is : {age} \n and his / her  percentage in hsc is : {hsc}  ")
# creating variables 
a = 15 
b = 4 
print("simple mathematic calculation " )
print( "sum",a+b)
print( "difference",a-b)
print( "product",a*b)
print( "division",a/b)
height: float = 5.8
bloodtype: str = "a+"
roll_no: int = 32
is_student: bool = True

print (type(height),
       type(bloodtype),
       type(roll_no ) ,
       type(is_student) ,
       )
name1 = input("enter your name ")
age1 = int(input("enter your age , plz dont shy "))
# change data type and add 50 
print(f"so basically ur name is {name1 } and ur {age } years old 👀👀" )
print("changing the data type string to int  and adding 50 ")
c = "100"
print(int(c)+50)
# swap to num using 3rd veriable 
d = 10

e = 11
temp = d

d = e
e = temp

print(f"d ={d} and e= {e}")










