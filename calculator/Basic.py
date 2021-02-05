#Hello world
print('Hello world')

#Variables and data types
character_name = "George"
character_age = "14"
print('There once was a man named' + character_name +',')
print('he was 70 years old.')
character_name = "Mike"
print("He really liked the name" + character_name +".")
print('but didn`t like being' + character_age + '.')

#strings
character_age = 50.9707 # does not require ""
is_Male = False #boolen

print("Hello\nthere")
print("Hello\"there")
print("Hello\there")
phrase = "Hello there"
print(phrase)
#concatination
print(phrase + ' how are you')

#functions
phrase = "Hello there"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("h"))
print(phrase.index("the"))
print(phrase.replace("Hello", "Hey"))

#working with numbers
print(-456)
print(8+4) #can do all basic arithmetic operation
print(3 * 4 + 5) # follows the rule of bodmas
print(3 * (4 + 5))
print(10 % 3) #modulus
my_num = 5
print(my_num)
print(str(my_num) + " is now a string") #converting a number to string

#numerical operations
my_num = -5
print(abs(my_num)) #absolute value
print(pow(3,4)) #3 raised to power 4
print(max(6,8))
print(min(5,8))
print(round(3.6))
#importing external code
from math import *
print(floor(8.9)) #lower whole number
print(ceil(5.7)) #higher whole number
print(sqrt(9))
#just a few of math functions. Google the others

#getting input from a user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
