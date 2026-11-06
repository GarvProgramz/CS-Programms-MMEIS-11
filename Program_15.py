#Program to create a dictionary with the roll number as the key & name & mark as values. Display the name of students who have marks above 75.
student={} 
n=int(input("Enter the limit = "))
for i in range(n):
  rno=int(input("Enter the roll number = "))
  name=input("Enter the name = ")
  mark=int(input("Enter the marks = "))
  student[rno]=[name,mark]
print(student)
for i in student:
  if student[i][1]>75:
    print(student[i][0]) 
