name={'name':'santhiya','age':20,'department':'INFORMATION TECHNOLOGY'}
length=len(name)
print(length)
student={'id':103,'course':'pyhton'}
name.update(student)
print(name)
copy=name.copy()
print(copy)
marks={'santhiya':100,'paulthinakaran':99,'vijaya':101}
print(max(marks.values()))
print(min(marks.values()))
sum=0
for i,j in marks.items():
    sum=sum+j
print(sum)
age={'san':2,'rob':3,'cath':4,'paul':5,'thianakaran':6,'vijaya':7}
x={}
k=0
for i,j in age.items():
    if j%2==0:
        x[k]=j
        k=k+1
print(x)
x={'name':'santhiya','age':20,'department':'INFORMATION TECHNOLOGY'}
y={}
for i,j in x.items():
    y[j]=i
print(y)
student={'name':'santhiya','age':20,'department':'INFORMATION TECHNOLOGY'}
sorted_dict=dict(sorted(student.items()))
print(sorted_dict)
student={'santhiya':100,'robin':90,'cathrin':80}
sorted_dict=dict(sorted(student.items(),key=lambda x: x[1]))
print(sorted_dict)

fruit='banana'
x=input("enter a charecter")
count=0
for ch in fruit:
    if ch in x:
        count=count+1
print(count)
    
    

    

    
