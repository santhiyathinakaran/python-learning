student={'name':'santhiya','age':20,'department':'INFORMATION TECHNOLOGY'}
print(student)
print(student.keys())
print(student.values())
for i,j in student.items():
    print(i,j)
print(student['name'])
value=input("enter the key:")
for i,j in student.items():
    if i == value:
        print(i,j)
student['roll no']=103
print(student)
student['name']='sandy'
print(student)
student.pop('age')
print(student)
student.popitem()
print(student)
del student['name']
print(student)
student.clear()
print(student)
  
