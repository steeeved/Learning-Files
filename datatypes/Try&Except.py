number = int(input("Enter a number: "))
print(number) # if the user does not enter a number, the program fails

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err) # use this, its a good practice to catch specific errors
except ValueError:
    print("Invalid input")