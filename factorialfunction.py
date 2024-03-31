#factorial
n=int(input("Enter a number "))
i=1
f=1
while(i<=n):
    
    f*=i
    i+=1
print("factorial=",f)    
print();




#2 functionfactorial
n=int(input())
def fact(n):
    f=1
    if n==0:
        print("Factorial:",1);
    else:
        for i in range(1,n+1):
            f*=i
        print("Factorial:",f);
fact(n)
fact(6)



#3
n=int(input())
def fact(n):
    f=1
    if n==0:
        print("Fcatorial:",1);
    else:
        for i in range(1,n+1):
            f*=i
        return f;
o=fact(n)
print("Factorial:",o);
p=fact(6)
print("Factorial:",p);
