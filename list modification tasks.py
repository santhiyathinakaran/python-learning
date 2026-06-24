list=[1,2,3,4,5,6,7,8]
list.append(9)
print(list)
list.insert(9,10)
print(list)
list.remove(3)
print(list)
list=[2,4,6,8,10,1,3,5]
list[0]=1
print(list)
list=[1,2,3,4,5,6,7,8]
list[0],list[7]=list[7],list[0]
print(list)
l=[1,2,3,4,5,6,7]
x=int(input("Enter the numbers:"))
y=int(input("Enter the number:"))
l[x],l[y]=l[y],l[x]
print(l)
