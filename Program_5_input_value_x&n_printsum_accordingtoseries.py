#Part A - 1 + x + x² + x³... xⁿ
x = int(input("Enter the value of x = "))
n = int(input("Enter the value of n = "))
s = 0 
for i in range (n+1):
  s+=x**i
print ("Sum is",s)
#Part B - 1 - x - x² - x³... xⁿ
x = int(input("Enter the value of x = "))
n = int(input("Enter the value of n = "))
s1 = 1
for i in range (1, n+1):
  s1 -= x**i
print ("Sum is", s1)
#Part C - x + x/2 + x/3 +... x/n
x = int(input("Enter the value of x = "))
n = int(input("Enter the value of n = "))
s2 = 0
for i in range (1, n+1):
  s2 += x/i
print ("Sum is", s2)
#Part D - x + x/2! + x/3! +... x/n!
x = int(input("Enter the value of x = "))
n = int(input("Enter the value of n = "))
s3 = 0
fact = 1
for i in range (1, n+1):
  fact = fact*i
  s3 += x/fact
print ("Sum is", s3)
