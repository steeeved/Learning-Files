employee_file = open("employees.txt", "r")#reading info
#print(employee_file.readable())
#print(employee_file.read())
print(employee_file.readlines()[2])