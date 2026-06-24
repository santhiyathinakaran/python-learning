list=[2,3,4,5,6,7,8,9]
num=int(input("enter the number:"))
for i in list:
    if i==num:
        print("the number  is in the list")
    else:
        print("not available")
num=[3,4,5,67,7,8,9]
num1=int(input("Enter the number:"))
if num1 in num:
        print(num.index(num1))
else:
        print("not in num")
num=[3,4,5,67,7,8,9,9,9,9,4]
x=num.count(9)
print("occurrences of the given number is:",x)

num=[3,4,5,67,7,8,9,9,9,9,4]
target=int(input("enter the number"))
position=[]
for i in range(len(num)):
        if num[i]==target:
                position.append(i)
print(position)
num=[3,4,5,67,7,8,9,9,9,9,4]
duplicate=[]
for i in num:
        if num.count(i)>1 and i not in duplicate:
                duplicate.append(i)
                print(duplicate)
                
