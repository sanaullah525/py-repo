"""
 demo.py
 Simple Python scripts to demonstrate print statements
  and basic arithmetic operations.
"""

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

var= 233
print(var +2, "\n")
print("\n")


'''
The first program
'''

'''
 #...This program says and asks for my name.
print("Hello world!")
print("What's your name ?") # Ask for their name.
myName= input()
print("It's good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName),"\n")
print("What's your age ?") # Ask for their age.
myAge= float(input())
print(f"You will be {myAge + 1} in a year.\n")

print() 
'''

print()

name = "Sanaullah"
print(f"My name is {name}")
print()

pi= round(3.14159)
print(pi)
print(type(pi))


#...Boolean Logic in python.
print(45 == 45.0)

print(34 == '34')

print(90 == 0090.00)
print()

bacon= 20
print(bacon + 1)
print(bacon)

print('spam' + 'spamspam')
print('spam' * 3)
print()

total_burritos= 99
print('I have eaten ' + str(total_burritos) +
       ' burritos.')
print()

#...Boolean values, comparison operators, and Boolean operators.
spam= True
print(spam)

print(34 == 23)
print(2 != 3)
print(2!= 2)
print()

#...Comparison operators
eggcount= 42
print(eggcount <= 42)
myage= 26
print(myage >= 10)
print()

###...Boolean operators...###
#..AND operator
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

#..OR operator
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

#..Mixing Operators
print(not True)
print((not False) and True)
print((not False) or False)
print((not True) or False)
print(True or False)
print(False and True)
print(True and False)

print(not True)
print(not False)
print() 
                """

'''
#...Mixing Boolean and Comparison Operators
print((4 < 5) and (5 < 6))
print((4 < 5) or (9 < 6))
print((1 == 2) or (2 == 1))
print()

print('dog' != 'cat')
print('dog' == 'cat')
print()


print("What is your name ?")
name= input()
if name == 'Alice':
  print(f"It's good to meet you, {name}.")
'''
print()


'''
print('What is your name?')
nam= input()
if nam == 'Alice':
  print(f'Nice to meet you, {nam}')
else:
  print('Hello, stranger.')
print()
'''

'''
print('What is your name ?')
nom= input()
print(f'What is your age ?')
sokalan= float(input())

if nom== 'Sanaullah Khan' and sokalan== 26:
  print(f'Welcome, Sir',nom)
elif sokalan < 26:
  print('You are not him. kiddo')
elif sokalan == 26:
  print('Welcome, Sir')
'''
  
'''
pswd = "swordfish"
print('Type password')
pswd= input()
print()

if pswd == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password !')
'''

'''
#...elif examples.
print('What is your name ?')
name= input()
print()
print('How old are you ?')
age= int(input())

if name != 'Alice':
    print('Unauthorized access denied!.')
elif name == 'Alice' and age == 12:
    print('Hi Alice.')
elif age < 12:
    print('Have you done your homework ?',"Get off the PC 😖. Right now!!!")
elif age > 49:
    print("You're nor Alice granny.")
elif 49 < age < 125:
    print('You are definitly not Alice. Kindly turn the PC off!')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
else:
    print('You are not Alice at all...')
'''



#...Nested statements.
print('What is your name ?')
name= input()

if name != 'Alice':
    print('Access denied!')
else:
  print('How old are you ?')
  age= int(input())
  print()

  if name != 'Alice':
      print('You are not Alice at all.')
  elif name == 'Alice' and age == 12:
      print('Hi Alice, please enter your password')
  elif age < 12:
      print('Have you done your homework ?',"Turn off the PC. Right now!!!")
  elif age > 49:
      print("You're not Alice granny.")
  elif 12 < age < 49:
      print('Access denied!\nYou are not an authorized person.')
  elif age > 2000:
      print('Unlike you, Alice is not an undead, immortal vampire.')