def is_armstrong(n):
    num = n
    result = 0
    n = len(str(n))
    while(num != 0):
        digit = num % 10
        result = result + digit ** n
        num = num // 10
    return result == n

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
