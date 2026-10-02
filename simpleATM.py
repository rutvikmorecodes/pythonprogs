"""Project 3: Simple ATM
Store an initial account balance.
Display options to check balance, deposit, and withdraw.
Use loops and conditions to keep the menu running.
Use functions for each operation.
Prevent withdrawals greater than the available balance."""
import random 
acBAL = random.randint(10000, 100000)
def menu(acBAL):
    
    opt  = int(input("enter the number to check 1. check balance, 2. deposite, 3 . withdrawal, 0. enter any digit for exit  "))


    if opt == 1:
        print("balace is " , acBAL)
    elif opt == 2:
        dep = int(input("enter amount for depositeS"))
        acBAL += dep
        print("balalce after deposite is : ",acBAL)
    elif opt == 3:
        witw = int(input("enter amount for withdrawal : "))
        if witw > acBAL:
            print("insufficient balance ")
        else:
            
                    acBAL -=witw
                    print("balace after withdrawal is ",acBAL)    

    else:
        return acBAL ,False
    return acBAL,True
running = True
while running:
     acBAL, running = menu(acBAL)


             

