
#employee_file = open("employees.txt", "r")#reading info
#print(employee_file.readable())
#print(employee_file.read())
#for employee in employee_file.readlines():
    #print(employee)
#print(employee_file.readlines()[2])
employee_file = open("employees.txt", "w") #writing the file
#employee_file = open("employees.txt", "a") #appending
employee_file.write("\n James -  Human resources")
#open("employees.txt", "r+") #reading and writing
employee_file.close()