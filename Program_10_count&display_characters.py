#Program to count and display the vowels, consonants, uppercase and lowercase characters in string.
s = input("Enter a string: ")

vowels = 0
consonants = 0  
uppercase = 0
lowercase = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
            
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of uppercase characters:", uppercase)
print("Number of lowercase characters:", lowercase)
