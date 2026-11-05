#Program to determine whether a string is Palindrome.
s = input("Enter a string: ")

if s.lower() == s[::-1].lower():
  print("The string is a palindrome")
else: 
  print("The string is not a palindrome")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Toggle case:", s.swapcase())
