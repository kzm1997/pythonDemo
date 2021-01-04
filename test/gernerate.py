import sys 
f=[ x for x in range(1,10)]
print(f)

for x in f:
    print(x)

f2=[x+y for x in 'ABCD' for y in'1234567' ]
print(f2)

f3=[x**2 for x in range(1,1000)]
print(sys.getsizeof(f3))
# print(f3)

f4=(x**2 for x in range(1,10000))
print(sys.getsizeof(f4))