a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
d=int(input("Enter a number "))
if(a>b):
   if(a>c):
       if(a>d):
           print("A is big ")
       else:
           print("D is big")
   else:
       if(c>d):
           print("C is big ")
       else:
           print("D is big")
else:
    if(b>c):
        if(b>d):
            print("B is big ")
        else:
            print("D is big")
    else:
        if(c>d):
            print("C is big ")
        else:
            print("D is big")
print("Thank You")
