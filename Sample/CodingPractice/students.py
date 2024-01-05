class Student():
    def __init__(self, roll=0, name="", marks=0):
        self.roll = roll
        self.name = name
        self.marks = marks


n = int(input("\nEnter No of Students: "))
students = []

for i in range(n):
    print("\nStudent %d details:\n" % (i+1))
    roll = int(input("Enter Roll: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students.append(Student(roll, name, marks))
   
sum = 0
for i in students:
    sum += i.marks

avg = sum/len(students)


    