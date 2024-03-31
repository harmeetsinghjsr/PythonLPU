#1
print("no return no arg")
def sum():
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
def sub():
    m=int(input())
    n=int(input())
    o=m-n
    print(o)
def multi():
    x=int(input())
    y=int(input())
    p=x*y
    print(p)
def div():
    u=int(input())
    v=int(input())
    w=u/v
    print(w)
sum()
sub()
multi()
div()
print("Thank You")



#2
print("no return yes arg")
def sum(a,b):
    c=a+b
    print(c)
def sub(m,n):
    o=m-n
    print(o)
def multi(x,y):
    p=x*y
    print(p);
def div(u,v):
    w=u/v
    print(w)
print ("outside function")
d=sum(7,8)
print("Sum=",d)
f=sub(10,20)
print("sub=",f)
g=multi(7,8)
print("multi=",g)
h=div(2,5)
print("div+",h)
print("Thank You")





#3
print("no return no arg")
def sum():
    a=int(input())
    b=int(input())
    c=a+b
    return c;
def sub():
    m=int(input())
    n=int(input())
    o=m-n
    return o;
def multi():
    x=int(input())
    y=int(input())
    p=x*y
    return p;
def div():
    u=int(input())
    v=int(input())
    w=u/v
    return w;
sum()
sub()
multi()
div()
print("Thank You")





#4
print("yes return yes args")
def sum(a,b):
    c=a+b
    return c;
def sub(m,n):
    o=m-n
    return o;
def multi(x,y):
    p=x*y
    return p;
def div(u,v):
    w=u/v
    return w;
print ("outside function")
d=sum(7,8)
print("Sum=",d)
f=sub(10,20)
print("sub=",f)
g=multi(7,8)
print("multi=",g)
print("Thank You")

