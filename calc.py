class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        n=self.a+self.b
        print("sum=",n)
    def sub(self):
        m=self.a-self.b
        print("sub=",m)
    def multi(self):
        o=self.a*self.b
        print("multi=",o)
p1=calc(2,3)
p1.sum()
p1.sub()
p1.multi()
