print("______WELCOME_______")
print()
print()
n=int(input("Enter a four digit number "))
print()
print()
d1=int(n%10)
n=n/10

d2=int(n%10)
n=n/10

d3=int(n%10)
n=n/10

d4=int(n%10)
n=n/10

sum=d1+d2+d3+d4
print("sum of four digits = ",sum)
print()
print()
rev=(d1*1000)+(d2*100)+(d3*10)+(d4)
print("reverse of the number = ",rev)
print()
print()
print("______THANK YOU________")
