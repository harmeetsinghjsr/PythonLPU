def fact(m):
    if m==0 or m==1:
        return 1;
    else:
        return (m*fact(m-1));
n=int(input("Enter a no."));
f=fact(n);
print("Factorial:",f)
