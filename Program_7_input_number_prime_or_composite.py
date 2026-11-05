#Program to input a number and check if the number is a prime or composite number.
n = int(input("Enter the number = "))
flag = 0
for i in range (2,n):
  if n%i==0:
    flag=1
if flag==0:
  print(n,"is a prime number.")
else:
  print(n,"is a composite number.")
