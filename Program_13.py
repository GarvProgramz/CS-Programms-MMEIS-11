#Program for list swapping of numbers in a list.
n=int(input("Enter the limit = "))
l=[]
for i in range(n):
  e=int(input("Enter the element = "))
  l.append(e)
print(l)
for i in range(0,len(l)-1,2):
  l[i],l[i+1]=l[i+1],l[i]
print(l) 
