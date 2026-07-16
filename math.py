a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))   
import math
def formu(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print(x)
        print(x2)
    elif d==0:
        x1=(-b)/(2*a)
        print(x1)
    else:
        print("the equqtion has complex roots ")
formu(a,b,c)
