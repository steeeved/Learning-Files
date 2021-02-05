num1 =input("Enter a number: ")
num2 =input("Enter another number: ")
result = num1 + num2

print(result)
#not the  answer expected.
# When promted to get an in input, python defautly converts it to a string

num1 =input("Enter a number: ")
num2 =input("Enter another number: ")
result = int(num1) + int(num2)
print(result)
#if the number is a float
# result = float(num1) + float(num2)
#print(result)

#BETTER CALCULATOR
num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")