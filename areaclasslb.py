'''class area:
    def __init__(self,pi):
        self.pi=pi
    def area_circle(self):
        r=int(input("Enter a radius:"))
        print("Area of circle:",self.pi*r**2)
class rectangle:
    def _init_(self,l,b):
        self.l=l
        self.b=b
    def area_rectangle(self):
        print("Area of rectangle:",self.l*self.b)
p1=area(3.14)
p1.area_circle() 
l=int(input('Enter length:'))
b=int(input("Enter breadth:"))  
p2=rectangle(l,b)
p2.area_rectangle()
'''


import math
class area:
    def display(self):
        print("Area is=",end=" ")
class circle(area):
    def _init_(self,r):
        self.r=r
    def cal(self):
        print(math.pi*(r**2))
class rectangle(area):
    def _init_(self,l,b):
        self.l=l
        self.b=b
    def cal1(self):
        print(l*b)
r=int(input())
l=int(input())
b=int(input())
obj=circle(r)
obj1=rectangle(l,b)
obj.display()
obj.cal()
obj1.display()
obj1.cal1()
