def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        return True
    if weekday == True and vacation == False:
        return False
    if weekday == False and vacation == True:
        return True
    if weekday == True and vacation == True:
        return False

print(sleep_in(True, True))

def string_times(str, n):
    times = str * n
    return times

print(string_times("Carol", 5))

def hello_name(name):
    return ("Hello "+ name +"!")

print(hello_name("Carol"))

def first_last6(nums):
    if nums[0] == 6:
        return True
    elif nums[-1] == 6:
        return True
    else:
        return False

print(first_last6([6,2,7]))

def double_char(str):
    to_return = ""
    for i in str:
        to_return += i*2
    print(to_return)

double_char("The")


def count_evens(nums):
    x = 0
    for i in nums:
        if i % 2 == 0:
            x += 1
    print(x) 

count_evens([3,3,3,33,3])