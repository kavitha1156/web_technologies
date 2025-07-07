hii
# comments

#print("python programming")

""" python is high level object oriented programming language"""

""" variables::"""
"""aa=10
print(aa)

num=10,20,30
print(num)

a=b=c=100
print(a,b,c)

a1,b1,c1=10,20,30
print(a1,b1,c1)"""

# #keywords::

# import keyword
# print(keyword.kwlist)

#id()::
"""a=10
b=133.07
c=10+34j
print(type(a))
print(type(b))
print(type(c))"""

#input()::
"""num1=int(input("enter  an integer number"))
num2=float(input("enter  a float number"))
result=num1+num2
print(result)
"""
#datatypes::
"""a=1
print(bool(a)) 

for i in range(1,10):
    print(i) 

for i in range(20):
    print(i)

for i in range(20,0,-2):
    print(i) 

    infinate loop:
i=0
while i<20:
    print(i)
    i++

i=0
while i<20:
    print(i)
    i+=1 

str1="kavitha"
print(str1[-1])
print(str1[0:])
print(str1[-1:])
print(str1[::-1]) 
str1="kavitha"
print(str1[-1::0])"""

def fact(a):
    if a<=1:
        return 1
    else:
        return a*fact(a-1)
kk=fact(5)
print(kk)







