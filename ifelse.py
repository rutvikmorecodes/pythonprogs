#Check whether a number is positive, negative, or zero.
num = int(input("enter a number "))
if num > 0:
    print("number is positive ")
elif num < 0:
    print("number is negative")
else:
    print("number is ")        

#Check whether a person is eligible to vote based on age.
age = int(input("enter your age "))
if age >= 18:
    print("eligible for voting")
else:
    print("not aligible for voting")    

#Take three numbers and print the largest.
Tnum = input("three number use space after number  ").split()
a = Tnum[0]
b = Tnum[1]
c = Tnum[2]

if a >= b and a >= c:
    print(f"{a} : a is largest")
elif b >= a and b >= c:
    print(f"{b} : is largest ")
else:
    print(f"{c} : is largest " )        


#Create a grading system based on marks:
per = int(input("enter your percentage "))
if per >= 91:
    print("passed by A1 grade ")
elif per >= 81 and per <= 90 :
    print("paases by A2 grade")

elif per >= 71 and per <= 80 :
    print("paases by B1 grade")

elif per >= 61 and per <=70 :
    print("paases by B2 grade")    

elif per >= 51 and per <=60 :
    print("paases by C1 grade")

elif per >= 41 and per <=50 :
    print("paases by C2 grade") 

elif per >= 33 and per <=40 :
    print("paases by D grade") 

else : 
    print("paases by FAIL grade")             



#Check whether a year is a leap year.
year = int(input("inter year to check leap or not "))
if year % 4 == 0:
    print(f"year {year} is leap year")
else:
    print("year is not leap year")    

#Create a calculator using if-elif-else that supports +, -, *, and /.
num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2st number : "))
op = input("enter operator + , - , / , *  :  ")
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)

elif op == "/":
    print(num1/num2)

else:
    print(num1*num2)




#Check whether a character is a vowel or consonant.
ch = input("enter a charector ").lower()
if ch in "eiou":
    print("vowel")
else:
    print("consonant")    


#Create a login system that checks a username and password.
#ceating database here 
username ="rutik" 
password = "rutik@123"
un = input("enter username ")
ps = input("enter password")
if un == username and ps == password:
    print("logined in succesfully")
else:
    print("username or password incorrect")    