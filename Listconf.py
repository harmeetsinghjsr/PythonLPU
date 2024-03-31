#1 
def print_ok(L):
    for x in L:
        if x==10:
            print("TEN")
        elif x==20:
            print("TWENTY")
        elif x==30:
            print("THIRTY")
        elif x==40:
            print("FOURTY")
        elif x==50:
            print("FIFTY")
l1 = [10,20,30,40,50]
print_ok(l1)

#FACTORIAL LIST

def print_ok(L):
    s = 1
    for i in L:
        s = s*i
        print(s)
l1 = [1,2,3,4,5]
print_ok(l1)





#2
def Print_Contents_List(L):
    for x in L:
        if x%2==0:
            print("even=",x)
        else:
            print("Odd=",x)
    
L1=[10,21,30,47,50]
Print_Contents_List(L1)
