#Program to display the terms of the Fibonacci series.
n=int(input("Enter the number = "))
a=0
b=1
print("The Fibinacci series is")
for i in range(n):
  print(a,end=" ") 
  a, b = b, a + b
