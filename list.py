"""Create a list of five numbers. Print the largest, smallest, and sum of all numbers.

Add an element to a list, remove an element, and update an existing element.

Reverse a list without using the reverse() method.

Count how many even and odd numbers are present in a list.

Find the second-largest number in a list.

Remove duplicate elements from a list.

Create a new list containing only numbers greater than 10 from an existing list.

Sort a list in ascending and descending order.

Find the common elements between two lists.

Create a list of student marks and calculate the average marks."""
num = [6,3,7,5,9,]
print(len(num),"is the lenght of list")
lar = max(num)
small = min(num)
print(small,"is smallest element of the list")
print(max(num), "is largest number in above list")
print(sum(num), " is sum of all numbers ")
#adding element
print("adding new element to list")
num.append(44)
print(num)
# removing the element from the list

print("removing new element to list")
num.remove(6)
#replcing the element from the list
num[0] = 45
print("final list after all operations")
print(num)
print(num[::-1], "this is reverse version of list")
#count how many even and odd nums are in list
even = 0
odd = 0

for i in range(len(num)):
    if num[i] % 2 == 0:
        even += 1

    else :
        odd += 1
print(f"there are {even} even number and {odd} odd numbers ")        
#finding 2nd largest number in list
num.sort()
print(num[len(num)-2])
# removing duplicate numbers from list
num1 = [6,3,7,5,9,9,9,9]

removedD = list(set(num1))

print(removedD)
# removing duplicate numbers from list withou list(set()) function
for i in range(len(num1) - 1 ,0 , -1):
  if num1[i] ==  num1[i-1]:
      num1.pop(i)

print(num1)  
print(f"this {num1} is final list num1") 
# creating a list that contains numbers greater than 10 from previous list num1


for i in range(len(num1)):
    if num1[i] >=  10:
         num1

    else:
         num1[i] = num1[i] +  10

print(num1)

for i in range(len(num1)-1):
    if(num1[i] > num[i + 1]):
        num1[i] ,num[i + 1]= num[i + 1],num1[i]
print(num1,"this is assending sorted list ")           
"""for i in range(len(num1) - 1):
    if num1[i] > num1[i + 1]:
        num1[i], num1[i + 1] = num1[i + 1], num1[i]"""
count = 0
for i in  range(len(num1)):
    for j in  range(len(num)):
        if num1[i] == num[i]:
            print("common element is ",num1[i])
            count += 1

# new             

if count == 0:
    print("not an single comman  element in lists ")
marks = []
marks = 34
print(marks)
tot = sum(marks)
print(tot)
def avgM():
    avg = tot/len(marks)
    print(avg)
avgM()    

          

        