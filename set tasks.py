x={1,2,3,4,5}
x.add(6)
print(x)
y={7,0,4,6,7}
x.update(y)
print(x)
x.union(y)
print(x)
z=x.intersection(y)
print(z)
q=x-y
print(q)
h=x^y
print(h)
x.remove(1)
print(x)
x.discard(1)
print(x)
x.pop()
print(x)
a={10,20,30,40,50}
b={10,20}
print(b.issubset(a))
c={1,2,3}
d={10,20}
print(d.issuperset(c))
print(c.isdisjoint(d))
m=a.copy()
print(m)
a.clear()
print(a)



