#Part A - To determine if a number is a perfect number or not.
n=int(input("Enter the number = "))
print("Checking for perfect number...")
perfect=0 
for i in range(1,n):
  if n%i==0:
    perfect+=i
if n==perfect:
      print(n,"is a perfect number.")
else:
      print(n,"is not a perfect number.")
#Part B - To determine if a number is an Armstrong number.
n=int(input("Enter the number = "))
print("Checking for Armstrong number...")
arm=0
temp=n
n1=len(str(n))
while temp>0:
  r=temp%10
  arm+=r**n1
  temp=temp//10
if arm==n:
    print(n,"is an armstrong number.")
else: 
    print(n,"not an armstrong number.")
#Part C - To determine if a number is a Palindrome number.
n=int(input("Enter the number = "))
print("Checking for Palindrome number...")
temp1=n
palin=0
while temp1>0:
  r1=temp1%10
  palin=palin*10+r1
  temp1=temp1//10
if palin==n:
    print(n,"is palindrome.")
else: 
    print(n,"is not a palindrome.")
