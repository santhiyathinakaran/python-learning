#count the occurrece of each element

x=[1,2,3,4,2,3,5,6]
count = {}
for i in x:
    if i in count:
       count[i]=count[i]+1
    else:
        count[i]=1
print(count)

#find duplicates element

x=[1,2,3,4,2,3,5,6]
count = {}
for i in x:
    if i in count:
       count[i]=count[i]+1
    else:
        count[i]=1
print(count)
for key,values in count.items():
    if values>1:
        print(key)

#remove duplicates values


x=[1,2,3,4,2,3,5,6]
count = {}
for i in x:
    if i in count:
       count[i]=count[i]+1
    else:
        count[i]=1
print(count)
for key,value in list(count.items()):
    if value>1:
        del count[key]
print(count)

#group words their first letter


m = ['apple','ant','banana','bat','boy','cat']
x=[]
for i in m:
    x.append(i[0])
print(x)
y=set(x)
print(y)
d={}
for i in y:
    tl=[]
    for j in m:
        if i==j[0]:
            tl.append(j)
            d[i]=tl
print(d)


#create simple phone book


phone={}
while True:
    choice=int(input("Enter a choice"))
    if choice==1:
        name=input("enter the name:")
        number=int(input("enter the number:"))
        phone[name]=number
        print(phone)
    elif choice==2:
        x=input("enter a name to search")
        if x in phone:
            print(name,':',phone[name])
        else: 
            print("the number is not found")
    elif choice==3:
        n=int(input("enter a number to update"))
        if name in phone:
            phone['san']=n
        print(phone)
    elif choice==4:
        for i,j in phone.items():
            print(i,j)
            break


#create dictionary based inventory system



inventory={}
while True:
    choice=int(input("Enter a the choice:"))
    if choice==1:
        name=input("enter the product name:")
        quantity=int(input("enter the quantity::"))
        inventory[name]=quantity
        print(inventory)
    elif choice==2:
        x=input("enter a name to search")
        if x in inventory:
            print(name,':',inventory[name])
        else: 
            print("the product is not found")
    elif choice==3:
        n=int(input("enter a quantity to update"))
        if name in inventory:
            inventory['rice']=n
        print(inventory)
    elif choice==4:
        s=input("enter a charecter to remove:")
        inventory.pop(s)
        print(inventory)
    elif choice==5:
        for i,j in inventory.items():
            print(i,j)
            break

#store employee details and search employee by id




employee={'e1':{'name':'san','department':'IT','salary':100000,'id':111},'e2':{'name':'sandy','department':'IT','salary':500000,'id':112},'e3':{'name':'santhiya','id':113,'department':'IT','salary':750000}}
print(employee)
for key,values in employee.items():
    x=int(input("enter a id"))
    if values['id']==x:
        print('name:',values['name'],
              'department:',values['department'],
              'id:',values['id'],
              'salary:',values['salary'])


#login system


x={'santhiya':12005,'sandy':1200,'san':1234}
name=input("enter the name:")
password=int(input("enter the password:"))
found = False
for key,values in x.items():
    if key==name and values==password:
        found=True
        print("login successfull")
        break
if not found:
    print("user not found")

#count the frequency


l=input("enter the number:")
num=[]
for i in l:
    num.append(int(i))
count={}
for i in num:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)



#average marks


mark={'tamil':99,'english':90,'maths':97,'science':99,'social':90}
print(mark)
total=0
for i,j in mark.items():
    total=total+j
print(total)
average=total/len(mark)
print(average)



        
