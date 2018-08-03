def a():
    return 5
print(a())     

# returns 5

def a():
    return 5
print(a()+a())     

#return 10

def a():
    return 5
    return 10
print(a())     

# return 5

def a():
    return 5
    print(10)
print(a())     

#return 5

def a():
    print(5)
x = a()
print(x) 

# prints 5 and none

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# print 8

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# prints "2"+"5" = "25"

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)  

# prints 100 and returns 10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))     

#would print 7 then 14 then 21

def a(b,c):
    return b+c
    return 10
print(a(3,5))

# would return 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  

# this would return 500,500,300, and 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# this would print 500 then 500 then 300 then 300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# prints 1 3 2

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

# prints1 3 5 10
