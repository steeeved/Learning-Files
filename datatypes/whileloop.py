i = 1
while i <= 10:
    print(i)
    i += 1 #also equal to i = i + 1

print("Done with loop")

#Building a guessing game
secret_word = "Carol"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): 
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!") 

#For loop

for letter in "Caroline Wanjiku":
    print(letter)

friends = ["Jim", "Karen", "Ubako"] #this is an array
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

friends = ["Jim", "Karen", "Ubako"] #this is an array
print(len(friends))
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")