"""
 demo.py
 Simple Python scripts to demonstrate print statements
  and basic arithmetic operations.
"""

print("Welcome to the python world !!!", 
      "This is my first demo script.",
    "Python is fun to learn and use.", "Happy coding!", 
        "Let's explore more Python features.")

#  Time for some arithmetic operations using python.
#  Addition, Subtraction, Multiplication, Division, 
# ... Integer Division, Modulus, Exponentiation
print("This is to print some arithmetics using python. ")
print("21+4= ", 21+4)
print("Multiplication: 7*6= ", 7*6)
print("Division: 56/8= ", 56/8)
print("Subtraction: 45-9= ", 45-9)
print("Integer Division: 22//7= ", 22//7)
print("Modulus: 29%5= ", 29%5)
print("Exponentiation: 3**2= ", 3**2)
print("That's all for now. More to come soon...\n")
print()

#...Some BODMAS rules.
print("Let's try some BODMAS rules now...")
print()
ba= (8*(25/5)-2)
print(ba, "\n")
ab= (30/5)*(22-6)/4
print(ab)


#...Now time for Data types
name = "Sanaullah"
age = 25
height = 5.4
is_student = True
skills = ["Python", "Data Analysis", "SQL"]

#...This prints the type of the data.
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(skills))

print()
#...This print() is used for a line break.


#...String concatenation and Replication.
print('Zerak ' + 'Khan')
print('Zerak' + "24", "\n")
'''This will result in a error.
Because we can't combine 
string values to an integer directly.'''

print('Zerak Khan  '*5)
'''This returns Zerak Khan 5 times.'''
print()

#...Storing Values in Variables.
spam= 40
print(spam)

eggs= 2
print(spam+eggs+spam)

spam= spam +2
print(spam)

