""" Take a string as input and print its length, first character, and last character.

Reverse a string using slicing.

Count how many times the letter "a" appears in a string.

Check whether a string is a palindrome. Example: madam.

Count the number of vowels in a string.

Take a full name and print it in uppercase, lowercase, and title case.

Replace all spaces in a sentence with hyphens.

Check whether a given word exists in a sentence.

Extract the first and last three characters of a string."""
string = input("enter your first name : ")
print("there are " , len(string), " letter  in your name ")
print("and " , string[0], "is 1st letter in your name "  )
print("and ",string[ len(string)-1]," is last letter of your name")
print(string[::-1])
print(string.count("a"))
if string == string[::-1] :
    print("string is palindrome")
else :    
    print("string is not palindrome")


name = input("enter full name : " ,)


print(name.upper(), "is upper case of ur name ")
print(name.lower(), "is lower case version")
print(name.title(),"this one is title case version of ur name " )
clg = input("enter college name ")
print(clg.replace(" " , "-"))
checkword = input("enter college's any word that included in college or word that u want find in college name  ")
if checkword in clg :
    print("word exists in clg ")
else : 
    print("word not exists ")    




