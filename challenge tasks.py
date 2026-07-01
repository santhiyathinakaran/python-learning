num=[1,2,3,4,5,6,8,9,10]
i = 1
while i <= 10:
    if i not in num:
        print(i)
    i=i+1
print("**************************************************")
  
x=[1,2,3,4,5,6,7,8,9,1,2,3,3]
y=set(x)
print(y)
print("**************************************************")
x=[2,3,4,5,1]
y=[1,3,2,4,5]
if x.sort()==y.sort():
    print("it contain same elements")
else:
    print("it does not contain same elemants")
print("*************************************************")
a={1,2,3}
b={3,4,5}
c={3,5,6}
d=a&b&c
print(d)
print("**********************************************")
number=[2,3,4,34]
i=0
while True:
    menu=int(input("enter a value"))
    if menu==1:
        number.append(25)
        print(number)
    elif menu==2:
        number.remove(34)
        print(number)
    elif menu==3:
        print(number)
    else:
        break
print("********************************************************")    
        
number={2,3,4,34}
i=0
while True:
    menu=int(input("enter a value"))
    if menu==1:
        number.append(25)
        print(number)
    elif menu==2:
        number.remove(34)
        print(number)
    elif menu==3:
        print(number)
    else:
        break
print("*****************************************************")
number=[2,3,4,2,3]
num=[]
for i in number:
    if i not in num:
        num.append(i)
print(num)
print("*****************************************")
name=input("enter the sentence:")
split=name.split()
print(split)
x=set(split)
print(x)
print("***************************************************")
s1=(101,'santhiya','IT',99)
s2=(102,'paul','IT',98)
s3=(103,'vijaya','IT',100)
s4=(104,'robin','IT',97)
s5=(105,'cathrin','IT',96)
s=[s1,s2,s3,s4,s5]
print(s)
l=[]
for i in s:
    l.append(i[3])
print(l)
maxmark=max(l)
print(maxmark)
position=l.index(maxmark)
print(s[position])

