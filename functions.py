# 1. Create a function `greet()` that prints `"Hello, World!"`.
def greet():
    print("hello, world")
greet()    
 
# 2. Create a function that takes a name as an argument and returns a greeting.
def greet1(name):
    return "hello " + name
print(greet1("rutik"))

# 3. Create a function that takes two numbers and returns their sum.
def cal():
   
    
   a = int(input("enter 1st number : "))
   b = int(input("enter 2st number : "))
   print(f"{a+b} : is the sum of number {a} and  {b} ")
cal()   
    # 4. Create a function that checks whether a number is even or odd.
def ckN():
    num = int(input("enter number for check number is even or odd : "))

    if num % 2 == 0:
        print(f"number {num} is even ")
    else:
        print(f"number {num} is odd ")
ckN()       

# 5. Create a function that returns the factorial of a number.
def fac():
    fc =1
    nf = int(input("enter a number for factorial : "))
    for i in range(1,nf+1):
        fc = fc * i
    
    print(f"{fc} is factorial of num {nf}")

fac()

# 6. Create a function that checks whether a number is prime.
def prime():
    pr = int(input("enter number to check num prime of not : "))
                   
    if pr < 2:
        print(f"number {pr} is not prime")
    else:
        for i in range(2,pr):
            if pr % i == 0:
                print(f"number {pr} is not prime")
                break
        else:
            print(f"{pr} number is prime ")        
prime()

# 7. Create a function that takes a list and returns its largest element without using `max()`.
li = list(map(int,input("enter numbers for list  ").split()) )
large = li[0]
def larg(li,large):
    
    
    for i in li:
        if i > large:
            large = i
    return large
        
print(f"{larg(li,large)} : is largest element of li list")


larg(li,large)

# 8. Create a function that counts vowels in a string.
def cnt():
    s = input("enter a string for a count vowels or  consonants ")
    count = 0
    for i in s:
        if i in "aieou":
            print(i)
            count += 1
        
    print(f"there are {count} vowels in cnt string")                

cnt()
# 9. Create a function with a default parameter for the country, such as `country="India"`.
def country(name,country1="india"):
    print(f"{name} loves {country1}")
country("rutik")    


# 10. Create a function that accepts any number of arguments using `*args` and returns their sum.
def sum(*a):
    sum = 0
    for i in a:
        sum += i
    return sum
print(sum(2, 3, 5))    



# 11. Create a function that accepts keyword arguments using `**kwargs` and prints them.
def KWA(**kwargs):
    print(kwargs)
KWA(name="rutik", age= 30, cls="bbaca")  
  


# 12. Create a recursive function to calculate the factorial of a number.


# 13. Create a lambda function that squares a number.

# 14. Use `map()` with a lambda function to double every number in a list.

# 15. Use `filter()` with a lambda function to get only even numbers from a list.