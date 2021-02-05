# help organise code
def say_hi(): #using underscore is a good practice. name using lowerxcase letters
    print("Hello user")

print("Top")
say_hi() #flow of functions
print("Bottom")

def say_hi1(name):
    print("Hello " + name)

say_hi1("Steve")

def say_hi2(name, age):
    print("Hello " + name + ", you are " + age + " years old")

say_hi2("Carol", "20")
#you can pass alot of different data types

#RETURN STATEMENT
def cube(num):
    return num * num * num # cannot put any code below the return function

result = cube(4)
print(result)

#If statements

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_female = True
is_tall = True
if is_female or is_tall: #executes if one or both are true
    print("you are female or tall or both")
else:
    print("you neither male nor tall")

if is_female and is_tall: #executes if both are true
    print("you are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and (is_tall):
    print("You are not a female but are tall")
else:
    print("you either not a female or not tall or both")

#if statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(3,40,80))

 