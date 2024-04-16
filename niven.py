def is_niven_number(num):
    return num % sum(int(digit) for digit in str(num)) == 0

# Test the function
print(is_niven_number(18))  # True
print(is_niven_number(19))  # False
