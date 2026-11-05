#Program to compute the greatest common advisor and least common multiple of two integers.
a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))

x = a
y = b

while y!= 0:
 x, y = y, x % y

gcd = x
lcm = (a*b)//gcd

print ("The Greatest Common Divisor is",gcd)
print ("The Lowest Common Multiple is",lcm)
