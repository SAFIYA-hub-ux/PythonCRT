dict={101:"pytg",102:"java",122323:"sql"}
print(dict)
print(type(dict))
print(dict[101])
print(dict.keys())
print(dict.values())
print(dict.items())

# keys(immutable),values(mutable)

# keys should be unique,
# if we mention the same key again the old key is overwritten,key should be immutable,
# we cant use list or dict in key

dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
print(dict)
print(dict["safi"])
#updating the element
dict["dqwd"]="dwefe"
print(dict)
print(len(dict))
print(dict.values())
print()
print(dict["dqwd"])
dict["safiioihi"]="dfrr"
print(dict)
dict.pop("madhu")
print(dict)
dict.popitem()
print(dict)
del dict["safi"]
print(dict)
for i in dict:
  print(i)


dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
for i in dict:
  print(i)

dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
for i in dict:
  print(dict[i])

dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
for i in dict:
  print(i,dict[i])

dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
print(dict)
x=dict.copy()
print(x)

dict={"safi":120,"madhu":978,"dqwd":9765,"madhu":897}
print(dict)
dict1={"cdc":909,"sd":9,9876:"dfdf"}
print(dict1)
dict1.update(dict)
print(dict1)
dict.update(dict1)
print(dict)



# 1. Write a python program to read the employee details as input from the user including employee name, employee number, designation, salary, department name, department number, manager name and print all the details using print statement.
# Reading employee details
employee_name = input("Enter employee name: ")
employee_number = input("Enter employee number: ")
designation = input("Enter designation: ")
salary = int(input("Enter salary: "))
department_name = input("Enter department name: ")
department_number = input("Enter department number: ")
manager_name = input("Enter manager name: ")

# Printing employee details
print("\n--- Employee Details ---")
print("Employee Name     :", employee_name)
print("Employee Number   :", employee_number)
print("Designation       :", designation)
print("Salary            :", salary)
print("Department Name   :", department_name)
print("Department Number :", department_number)
print("Manager Name      :", manager_name)

# 2. Write a python program to take n students details as input from the user including student name, student id, percentage and branch and note that you have to take the value of n input from the user

# Reading number of students
# 2. Write a python program to take n students details as input from the user including student name, student id, percentage and branch and note that you have to take the value of n input from the user

n = int(input("Enter the number of students: "))
students = []

# Reading each student's details
for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Student Name: ")
    student_id = input("Student ID: ")
    percentage = float(input("Percentage: "))
    branch = input("Branch: ")

    students.append({
        "Name": name,
        "ID": student_id,
        "Percentage": percentage,
        "Branch": branch
    })

# Printing all student details
print("\n--- Student Details ---")
for idx, student in enumerate(students, start=1):
    print(f"\nStudent {idx}:")
    print("Name       :", student["Name"])
    print("ID         :", student["ID"])
    print("Percentage :", student["Percentage"])
    print("Branch     :", student["Branch"])



n=int(input())

for i in range(n):
     print(f"\nEnter details for student {i + 1}:")
     name = input("Student Name: ")
     student_id = input("Student ID: ")
     percentage = float(input("Percentage: "))
     branch = input("Branch: ")
     print(name)
     print(student_id)
     print(percentage)
     print(branch)


n = int(input("Enter number of students: "))

names = []
ids = []
percentages = []
branches = []

# Input phase
for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    names.append(input("Student Name: "))
    ids.append(input("Student ID: "))
    percentages.append(float(input("Percentage: ")))
    branches.append(input("Branch: "))

# Output phase
print("\n--- Student Details ---")
for i in range(n):
    print(f"\nStudent {i + 1}:")
    print("Name       :", names[i])
    print("Student ID :", ids[i])
    print("Percentage :", percentages[i])
    print("Branch     :", branches[i])


x=input()
dict={}
y=x.count("A")
z=x.count("G")
a=x.count("C")
s=x.count("T")

dict["A"]=y
dict["G"]=z
dict["C"]=a
dict["T"]=s
print(dict)

x=input()
dict={}
for i in x:
    if 'A' in x:
      dict["A"]=x.count("A")
    if 'G' in x:
      dict["G"]=x.count("G")
    if 'C' in x:
      dict["C"]=x.count("C")
    if 'T' in x:
      dict["T"]=x.count("T")
print(dict)


count=int(input())
list=[]
list2=[]
for i in range(count):
  x=int(input())
  list.append(x)
print(list)
for i in list:
  if(i<5):
    y="underexpressed"
    list2.append(y)
  if i>=5 and i<=15:
    z="normal"
    list2.append(z)
  if(i>=15) :
    d="overexpressed"
    list2.append(d)
print(list2)

seq1=input()
seq2=input()
list=[]
for i in range(len(seq2)):
  if(seq1[i]!=seq2[i]):
    list.append(i)
print(list)

