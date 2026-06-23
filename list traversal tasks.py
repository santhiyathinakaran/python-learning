num=[1,-2,3,-4,5,6,7,-8,9,-10,12]
for i in range (len(num)):
    if i%2==0:
        print(num[i])
   
num=[1,-2,3,-4,5,6,7,-8,9,-10,12]
for i in range (len(num)):
    if i%2!=0:
        print(num[i])
   
num=[1,-2,3,-4,5,6,7,-8,9,-10,12]
print(num[::-1])
print(num[::2])
num=[1,-2,3,-4,5,6,7,-8,9,-10,12]
mid=len(num)//2
for i in range(mid):
    print(num[i])
num=[1,-2,3,-4,5,6,7,-8,9,-10,12]
mid=len(num)//2
for i in range(mid,len(num)):
    print(num[i])
num1=[2,4,6,8,9,0,10]
num=int(input("enter the number:"))
for i in num1:
    if i>num:
        print(i)
    
num1=[2,4,6,8,9,0,10]
num=int(input("enter the number:"))
for i in num1:
    if i<num:
        print(i)
    
    
num1=[2,4,6,8,9,0,10,15,20,30]
for i in num1:
    if i%5==0:
        print(i)
    
    
num1=[2,4,6,8,9,0,10,15,20,30]
for i in num1:
    if i%2==0 and i%3==0:
        print(i)
    
    
