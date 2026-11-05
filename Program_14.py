#Program to find number in list (linear search).
n=int(input("Enter the limit = "))
l=[]
for i in range(n):
  e=int(input("Enter the element = "))
  l.append(e)
print(l)
flag=0 
s=int(input("Enter the element to search = "))
for i in l:
  if i==s:
    flag=1
    ind=l.index(i) 
    break 
if flag == 1:
  print(s,"is found at index",ind) 
else:
  print(s,"is not found at index")
