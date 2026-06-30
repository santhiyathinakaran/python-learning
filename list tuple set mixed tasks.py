x=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
y=set(x)
print(y)
z=tuple(x)
print(z)
a=set(z)
print(a)
x=[1,2,3,4,5,6]
y=[2,3,4,6,7]
a=set(x)
b=set(y)
print(a)
print(b)
c=a.intersection(b)
print(c)
d=a^b
print(d)
mark=['jesus','san','rob','paul','dhina','viji','san','rob','cath','viji']
name=set(mark)
print(name)
mark1=(10,20,30,10,20,30,40,50,40,60)
mark=list(mark1)
print(mark)
count=0
for i in mark:
    count=count+i
print(count)
average=count/len(mark)
print(average)
team1={'san','paul','vijaya','thinakaran'}
team2={'san','rob','cath'}
team3=team1&team2
print("players in both teams",team3)
print("players only team A",team1)
print("players only team B",team2)
team4=team1|team2
print(team4)
print(len(team4))
x=list(team4)
print(x)
print(len(x))
y=tuple(x)
print(len(y))
print(y)
numbers=[]
i=0
while i<10:
    num=int(input("enter a number:"))
    i=i+1
    numbers.append(num)
print(numbers)
numbers.sort()
print(numbers)
x=tuple(numbers)
print(x)
y=set(x)
print(y)

