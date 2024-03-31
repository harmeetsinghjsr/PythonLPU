#1: Break Statement
print("Break Loop");
i=1 #starting of loop
while(i<10):#testing of loop
    print(i)#Box of statements
    if(i==5):
        break;
    i+=1 #incrementation line
print()
print()

    
#2:Continue in while loop
print("continue in while loop");
i=0
while(i<9):
    i+=1
    if(i==3):
        continue;
    print(i)
print()
print()

#3:Continue in for loop
print("Continue in for loop")
for i in range(9):
    if(i==3):
        continue;
    print(i)
print()
print()