#Part A - Generate star pattern using nested loops.
n = int(input("Enter limit = "))
for i in range(1, n + 1):
  for j in range(i):
    print("*", end="")
  print() 
#Part B - Generate number pattern using nested loops.
n = int(input("Enter the limit = "))
for i in range(n, 0, -1):
  for j in range(1, i + 1):
        print(j, end="")
  print()
  #Part C - Generate alphabet pattern using nested loops.
  n = int(input("Enter the limit = "))
for i in range (n+1):
  for j in range (i):
    print (chr(65+j),end="")
  print()
