#Program to find the largest and smallest number in a list.
n=int(input("Enter the limit = "))
l=[]
for i in range(n):
  e=int(input("Enter the element = "))
  l.append(e)
print(l)
print("The minimum element is",min(l))
print("The maximium element is",max(l)) 
