p=int(input('enter a number:'))
n=int(input('enter a number:'))
r=int(input('enter a number:'))
def tot(p,n,r):
    SI=p*n*r/100
    return SI
result=tot(p,n,r)
total=result+p
print(total)


y=input('enter a value:')
def num(y):
    rev=y[::-1]
    return rev
result=num(y)
print(result)
if y==result:
    print('the value id palindrome')
else:
    print("the value is consonent")

   

def num(n):
    for i in range(1,10):
        if i!=n:
            print(i)
            
num(3)
