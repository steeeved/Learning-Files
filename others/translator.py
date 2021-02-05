'''
Giraffe language
RULES
every vowel becomes a 'g'
------
dog -> dgg
cat -> cgt
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": # converting uppercase letters to lowercase
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))