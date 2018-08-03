'''
1) 

def a():
    return 5
print(a())       

input: a()
output: 5

2) 

def a():
    return 5
print(a()+a())       

input: a()
output: 5

3) 

def a():
    return 5
    return 10
print(a())        

input: a()
output: 15

4)  

def a():
    return 5
    print(10)
print(a())     

input: a()
output: 15

5)

def a():
    print(5)
x = a()
print(x)     

input: a()
output: 15

6)

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))   

input: a()
output: 15

7)

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

input: a()
output: 15

8)

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)  

input: a()
output: 15

9)

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))     

input: a()
output: 15

10)

def a(b,c):
    return b+c
    return 10
print(a(3,5))     

input: a()
output: 15

11)

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  

input: a()
output: 15

12)

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  

input: a()
output: 15

13)

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

input: a()
output: 15

14)

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

input: a()
output: 15
