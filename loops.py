"""Print numbers from 1 to 100 using a for loop."""
for i in range(1,101,2):

    print(i)
  

#Print all even numbers between 1 and 50.
for i in range(1,50):
    if i % 2 == 0:
       print(i)

#Print the multiplication table of a number entered by the user.
num = int(input("enter the number for table "))
for i in range(1,11):
    table = num * i
    print(table)


#Calculate the sum of numbers from 1 to n using a loop.

n = int(input( "enter the number : "))
sum = 0
for i in range(1,n + 1):
    

    sum = sum + i 
    print(sum)




#Calculate the factorial of a number using a while loop.

f = int(input("Enter a number: "))

fa = 1
i = 1

while i <= f:
    fa = fa * i
    i += 1

print(fa)
#Reverse a number using a loop. Example: 1234 → 4321.
num1 = int(input("enter number for reverse : "))
rev = 0
while 0 < num1:
    dig = num1 % 10
    rev = rev * 10 + dig
    num1 = num1 // 10
print(rev)    


#Count the number of digits in an integer.
num2 = int(input("enter the number : "))
count = 0
for i in str(num2):
    count += 1
print(count)
#Check whether a number is prime.
pr = int(input("enter a number to check its prime or not : "))
if pr < 2:
    print(f"{pr} : numbers is not prime ")
else:
    for i in range(2,pr):
        if pr % i == 0:
            print(f"{pr} : number is not prime")
            
            break   
        
    else:
            print(f"{pr} number is prime ")    
             
#Print all prime numbers between 1 and 100.
for i in range(1,100):
    for j in range(1,101):
        if j % i == 0:
            print("number is not prime ")
        break
    else:
        print("number is prime ")    


#Print the Fibonacci series for n terms.
nn = int(input("enter number for fibonacci of n ,  "))
a = 0
b = 1

for i in range(nn+1):
    print(a)
    a,b = b,a+b



#Print this pattern:  right angle triangle

for i in range(1,5):
    for j in range(i):
        print("*",end = "")
    print()
        
        
#Print this pattern: triangle right angle numbers
#  
"""
1 
12
123"""
for i in range(1,4):
    for j in range(1,i+1):
        print(j, end = "")
    print(" ")    
#Find the sum of all elements in a list using a loop, without using sum().
li = list(map(int,input("enter number for list use space instend of , : ").split()))
sum1 = 0

for i in li:
    sum1 = sum1 + i
print(sum1, ":  is the sum of li list")    

#find the maximum element in a list without using max().
print(max(li)," : is max element or highest element of li list")
