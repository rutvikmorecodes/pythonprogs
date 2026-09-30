"""Take student name and marks in five subjects.

Store marks in a dictionary.

Calculate total and percentage.

Assign a grade using conditions.

Create a function to display the report card."""

        

marks ={}
sn = input("enter the stud name ")
for i in range(6):
    sj = input("enter the subject name  ")
    mk = int(input("enter the marks for subject "))
    marks[sj]= mk
    if sj == "0":
        break

def tot(marks):
    t = 0
    
    for i in marks.values():
        t += i
    return t
total =tot(marks)
print(marks)

print(f"{total} : are total marks ")   
per = total / 6
print(f"{per} is percentage  of {sn} ")
def grade(per):
    if per >= 91:
        print(" O GRADE ")
    elif per >= 75 :
            print("A GRADE ")   
    elif per >= 60 :
                print("A GRADE ")   

    elif per >= 50 :
                print("B GRADE ")   

    elif per >= 35 :
                print("C GRADE ")   
    else :
                print("F GRADE ")   
grade(per)                
def reportC(marks):
    for subject, mark in marks.items():
        print(subject, ":", mark)

reportC(marks)
