#nested dictionary and display the student details by id

student={'name':'santhiya','id':1,'mark':100,'student2':{'name':'robin','id':2,'mark':99,'student3':{'name':'cathrin','id':3,'mark':98}}}
print(student)
student={"student1":{'name':'santhiya','id':1,'mark':100},'student2':{'name':'robin','id':2,'mark':99},'student3':{'name':'cathrin','id':3,'mark':98}}
x=int(input("enter a id:"))
for key,value in student.items():
    if value["id"]==x:
        print('name:',value['name'],
              'id:',value['id'],
              'mark',value['mark'])


#update
student={"student1":{'name':'santhiya','id':1,'mark':100},'student2':{'name':'robin','id':2,'mark':99},'student3':{'name':'cathrin','id':3,'mark':98}}
x=student['student2']['mark']=101
print(student)

#highest mark
student={"student1":{'name':'santhiya','id':1,'mark':100},'student2':{'name':'robin','id':2,'mark':99},'student3':{'name':'cathrin','id':3,'mark':98}}
h_mark=0
name=''
for key,value in student.items():
    if value['mark']>h_mark:
       h_mark=value['mark']
       name=value['name']
print(h_mark)
print(name)

#convert two list into dictionary
key=['name','age','mark']
value=['santhiya',20,100]
x=dict(zip(key,value))
print(x)

#squares

x={}
for i in range(1,10):
    key=i
    value=i*i
    x[key]=value
print(x)
    


        

