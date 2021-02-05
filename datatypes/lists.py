#put numbers boolen or even strings
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends =["Kevin", "Karen", "Carol", "Ebby", "Max"]
friends[1] = "Mike"
print(friends)
print(friends[1]) #accesing based on index
print(friends[-1])
print(friends[1:3])

#list functions
print(lucky_numbers)
#friends.extend(lucky_numbers)
friends.append("Steve")
friends.insert(1,"Marcos")
friends.remove("Carol")
friends.pop()
print(friends.index("Kevin"))
print(friends.count("Carol"))
friends.sort()
print(friends)
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)