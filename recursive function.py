def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))


def fab(n):
        if n<=1:
                return n
        else:
                return fab(n-2)+fab(n-1)
num=int(input('enter a number:'))
for i in range(0,num):
        print(fab(i),end=' ')

        
        
