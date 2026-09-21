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

# 6. Create a function that checks whether a number is prime.

# 7. Create a function that takes a list and returns its largest element without using `max()`.

# 8. Create a function that counts vowels in a string.

# 9. Create a function with a default parameter for the country, such as `country="India"`.

# 10. Create a function that accepts any number of arguments using `*args` and returns their sum.

# 11. Create a function that accepts keyword arguments using `**kwargs` and prints them.

# 12. Create a recursive function to calculate the factorial of a number.

# 13. Create a lambda function that squares a number.

# 14. Use `map()` with a lambda function to double every number in a list.

# 15. Use `filter()` with a lambda function to get only even numbers from a list.