try:
    b=int(input("enter the base:"))
    h=int(input("enter the height:"))
except:
    b=23
    h=2
else:
    print("else part")
finally:
    print("final part")
    area=1/2*b*h
    print(area)


try:
    num=int(input("enter the number:"))
except:
    num=2
if num%2==0:
    print('the number is even')
else:
    print('the number is odd')
























